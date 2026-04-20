from flask import Blueprint, render_template, session, redirect, url_for, flash
from app.models.schema import Categoria, Tema
from app.services import foro_service, usuario_service
from app.forms.foro_form import TemaForm, MensajeForm # Los crearemos en el paso 3

foro_bp = Blueprint('foro_route', __name__, template_folder='templates')

@foro_bp.route('/')
def index_foro():
    user = usuario_service.obtener_usuario_por_id(session.get("user_id"))
    categorias = Categoria.query.all()
    return render_template('foro/foro.html', categorias=categorias, usuario=user)

@foro_bp.route('/categoria/<int:id>')
def ver_categoria(id):
    categoria = Categoria.query.get_or_404(id)
    
    user = usuario_service.obtener_usuario_por_id(session.get("user_id"))
    
    temas = Tema.query.filter_by(categoria_id=id).order_by(Tema.fecha_creacion.desc()).all()
    
    return render_template('foro/categoria.html', categoria=categoria, temas=temas, usuario=user)

@foro_bp.route('/tema/<int:id>', methods=['GET', 'POST'])
def ver_tema(id):
    tema = Tema.query.get_or_404(id)
    user = usuario_service.obtener_usuario_por_id(session.get("user_id"))
    form = MensajeForm()

    if form.validate_on_submit():
        if not user:
            flash("Debes ser un cazador registrado para responder.", "error")
            return redirect(url_for('homeLogin_route.paginaLogin'))
        
        # Llamamos al service
        resultado, mensaje = foro_service.agregar_respuesta(
            usuario_id=user.id,
            tema_id=tema.id,
            contenido=form.contenido.data
        )
        
        if resultado:
            flash(mensaje, "success")
        else:
            flash(mensaje, "error")
            
        return redirect(url_for('foro_route.ver_tema', id=tema.id))

    return render_template('foro/tema.html', tema=tema, usuario=user, form=form)

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
        tema, mensaje = foro_service.crear_nuevo_tema(
            usuario_id=user.id,
            categoria_id=categoria_id,
            titulo=form.titulo.data,
            contenido=form.contenido.data
        )

        if tema:
            flash(mensaje, "success")
            return redirect(url_for('foro_route.ver_tema', id=tema.id))
        else:
            flash(mensaje, "error")

    return render_template('foro/crear-tema.html', form=form, categoria_id=categoria_id, usuario=user)