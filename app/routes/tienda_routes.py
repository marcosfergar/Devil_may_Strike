from flask import Blueprint, jsonify, redirect, render_template, request, session, url_for, flash


# importe formularios
from app.forms.tienda_form import ComentarioForm

# importe sercicios
import app.services.tienda_service as tienda_service
import app.services.usuario_service as usuario_service

tienda_bp = Blueprint('tienda_route', __name__, template_folder='templates')

@tienda_bp.route('/')
def ver_tienda():
    if "username" not in session:
        flash("Debes iniciar sesión para acceder a la tienda.", "error")
        return redirect(url_for('homeLogin_route.paginaLogin'))

    categoria_activa = request.args.get('categoria', 'all')
    pagina = request.args.get('page', 1, type=int)

    lista_productos = tienda_service.obtener_productos_paginados(categoria_activa, pagina, 10)
    user = usuario_service.obtener_usuario_por_id(session.get("user_id"))
    top_cazadores = usuario_service.obtener_ranking_usuarios(5)

    form = ComentarioForm()

    if user and user.is_guest:
            flash("Los invitados no tienen acceso a la tienda. ¡Regístrate para comprar!", "error")
            return redirect(url_for('homeLogin_route.paginaLogin'))
    

    return render_template('tienda.html',productos=lista_productos.items,paginacion=lista_productos, usuario=user, form=form, top_usuarios=top_cazadores, categoria_activa=categoria_activa)

@tienda_bp.route('/producto/<int:id>')
def detalle_producto(id):
    producto = tienda_service.obtener_producto_por_id(id)
    if not producto:
        flash("El producto no existe.", "error")
        return redirect(url_for('tienda_route.ver_tienda'))
    
    user = usuario_service.obtener_usuario_por_id(session.get("user_id"))
    form = ComentarioForm()
    
    return render_template('detalle-producto.html', producto=producto, usuario=user, form=form)

@tienda_bp.route('/producto/<int:producto_id>/comentar', methods=['POST'])
def postear_comentario(producto_id):
    if "username" not in session:
        return jsonify({"success": False, "message": "Sesión no iniciada"}), 401
    
    data = request.get_json()
    texto = data.get("contenido", "").strip()
    
    if not texto:
        return jsonify({"success": False, "message": "El comentario está vacío."})
    
    exito = tienda_service.agregar_comentario_producto(
        usuario_id=session.get("user_id"),
        producto_id=producto_id,
        texto=texto
    )
    
    user = usuario_service.obtener_usuario_por_id(session.get("user_id"))

    if exito:
        return jsonify({
            "success": True,
            "message": "¡Reseña forjada!",
            "autor": user.nombre,
            "contenido": texto
        })
    return jsonify({"success": False, "message": "Error al publicar."})


@tienda_bp.route('/comprar/<int:id>', methods=['POST'])
def comprar(id):
    if "username" not in session:
        return jsonify({"success": False, "message": "Sesión no iniciada"}), 401

    user = usuario_service.obtener_usuario_por_id(session.get("user_id"))

    if user and user.is_guest:
        return jsonify({"success": False, "message": "Los invitados no pueden comprar."})

    resultado = tienda_service.comprar_producto(user.id, id)
    
    if resultado["success"]:
        resultado["nuevos_orbes"] = user.orbes_rojos  # ya descontados tras la compra
    
    return jsonify(resultado)

@tienda_bp.route('/truco-orbes', methods=['POST'])
def truco_orbes():
    user_id = session.get("user_id")
    if not user_id:
        return jsonify({"success": False, "message": "Sesión no iniciada"}), 401

    if usuario_service.dar_orbes_truco(user_id, 1000):
        return jsonify({"success": True, "message": "¡JackPoot! +1000 Orbes"}), 200
    
    return jsonify({"success": False, "message": "Error al procesar el truco"}), 500