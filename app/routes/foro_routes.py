from flask import Blueprint, jsonify, render_template, request, session, redirect, url_for, flash
from app.services import foro_service, usuario_service
from app.forms.foro_form import TemaForm, MensajeForm

foro_bp = Blueprint('foro_route', __name__, template_folder='templates')

@foro_bp.route('/')
def index_foro():
    user = usuario_service.obtener_usuario_por_id(session.get("user_id"))
    categorias = foro_service.obtener_todas_las_categorias()
    return render_template('foro/foro.html', categorias=categorias, usuario=user)

@foro_bp.route('/categoria/<int:id>')
def ver_categoria(id):
    user = usuario_service.obtener_usuario_por_id(session.get("user_id"))
    categoria = foro_service.obtener_categoria_por_id(id)
    if not categoria:
            flash("La categoría no se pudo encontrar.", "error")
            return redirect(url_for('foro_route.index_foro'))
    
    temas = foro_service.obtener_temas_por_categoria(id)    

    return render_template('foro/categoria.html', categoria=categoria, temas=temas, usuario=user)

@foro_bp.route('/tema/<int:id>', methods=['GET', 'POST'])
def ver_tema(id):
    tema = foro_service.obtener_tema_por_id(id)
    if not tema:
        flash("El tema no se pudo encontrar.", "error")
        return redirect(url_for('foro_route.index_foro'))

    user = usuario_service.obtener_usuario_por_id(session.get("user_id"))
    form = MensajeForm()

    if form.validate_on_submit():
        if not user:
            flash("Debes ser un cazador registrado para responder.", "error")
            return redirect(url_for('homeLogin_route.paginaLogin'))
        
        resultado, mensaje = foro_service.agregar_respuesta(
            usuario_id=user.id,
            tema_id=tema.id,
            contenido=form.contenido.data
        )
        
        flash(mensaje, "success" if resultado else "error")
        return redirect(url_for('foro_route.ver_tema', id=tema.id))

    return render_template('foro/tema.html', tema=tema, usuario=user, form=form)

@foro_bp.route('/categoria/<int:categoria_id>/nuevo', methods=['GET', 'POST'])
def nuevo_tema(categoria_id):
    user_id = session.get("user_id")
    if not user_id:
        flash("Debes loguearte para publicar.", "error")
        return redirect(url_for('homeLogin_route.paginaLogin'))

    user = usuario_service.obtener_usuario_por_id(user_id)
    form = TemaForm()

    if form.validate_on_submit():
        tema, resultado = foro_service.crear_nuevo_tema(user_id, categoria_id, form.titulo.data, form.contenido.data)
    
        if tema:
            flash(resultado['texto'], resultado['categoria'])
            return redirect(url_for('foro.ver_tema', id=tema.id))
        else:
            flash(resultado, "error")

    return render_template('foro/crear-tema.html', form=form, categoria_id=categoria_id, usuario=user)

@foro_bp.route('/tema/<int:tema_id>/comentar-ajax', methods=['POST'])
def comentar_ajax(tema_id):
    user_id = session.get("user_id")
    if not user_id:
        return jsonify({"success": False, "message": "Inicia sesión primero"}), 401
    
    data = request.get_json()
    contenido = data.get("contenido")
    
    if not contenido or len(contenido.strip()) < 2:
        return jsonify({"success": False, "message": "El mensaje es muy corto"}), 400
    user = usuario_service.obtener_usuario_por_id(user_id)
    respuesta, info = foro_service.agregar_respuesta(user_id, tema_id, contenido)
    
    if respuesta:
        return jsonify({
            "success": True,
            "message": info["texto"],
            "puntos": info["puntos"],
            "autor_nombre": user.nombre,
            "autor_avatar": user.url_avatar,
        })
    return jsonify({"success": False, "message": info["texto"]}), 500