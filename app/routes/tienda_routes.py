from flask import Blueprint, jsonify, redirect, render_template, session, url_for, flash

# importe de rutas

# importe modelos
from app.database.db import db
from app.models.schema import Producto,Usuario

# importe formularios
from app.forms.tienda_form import ComentarioForm

# importe sercicios
import app.services.inventario_service as inventario_service
import app.services.tienda_service as tienda_service
import app.services.usuario_service as usuario_service

tienda_bp = Blueprint('tienda_route', __name__, template_folder='templates')

@tienda_bp.route('/')
def ver_tienda():
    if "username" not in session:
        flash("Debes iniciar sesión para acceder a la tienda.", "error")
        return redirect(url_for('homeLogin_route.paginaLogin'))
        
    lista_productos = tienda_service.obtener_todos_los_productos()

    user = usuario_service.obtener_usuario_por_id(session.get("user_id"))

    form = ComentarioForm()

    if user and user.is_guest:
            flash("Los invitados no tienen acceso a la tienda. ¡Regístrate para comprar!", "error")
            return redirect(url_for('homeLogin_route.paginaLogin'))
    
    return render_template('tienda.html', productos=lista_productos, usuario=user, form=form)

@tienda_bp.route('/producto/<int:id>')
def detalle_producto(id):
    producto = tienda_service.obtener_producto_por_id(id)
    if not producto:
        flash("El producto no existe.", "error")
        return redirect(url_for('tienda_route.ver_tienda'))
    
    user = usuario_service.obtener_usuario_por_id(session.get("user_id"))
    form = ComentarioForm()
    
    return render_template('detalle-producto.html', producto=producto, usuario=user, form=form)

@tienda_bp.route('/comprar/<int:id>')
def comprar(id):
    if "username" not in session:
        flash("Debes iniciar sesión para acceder a la tienda.", "error")
        return redirect(url_for('homeLogin_route.paginaLogin'))
        
    user = usuario_service.obtener_usuario_por_id(session.get("user_id"))

    if user and user.is_guest:
            flash("Los invitados no tienen acceso a la tienda. ¡Regístrate para comprar!", "error")
            return redirect(url_for('homeLogin_route.paginaLogin'))
    
    resultado = tienda_service.comprar_producto(user.id, id)
    
    if resultado["success"]:
        flash(resultado["message"], "success")
    else:
        flash(resultado["message"], "error")
        
    return redirect(url_for('tienda_route.ver_tienda'))

@tienda_bp.route('/producto/<int:producto_id>/comentar', methods=['POST'])
def postear_comentario(producto_id):
    if "username" not in session:
        flash("Debes iniciar sesión para acceder a la tienda.", "error")
        return redirect(url_for('homeLogin_route.paginaLogin'))
    
    form = ComentarioForm()
    if form.validate_on_submit():
        tienda_service.agregar_comentario(
            usuario_id=session.get("user_id"),
            producto_id=producto_id,
            texto=form.contenido.data
        )
        flash("Tu reseña ha sido forjada.", "success")
    
    return redirect(url_for('tienda_route.detalle_producto', id=producto_id))

@tienda_bp.route('/truco-orbes', methods=['POST'])
def truco_orbes():
    nombre_sesion = session.get("username")
    if not nombre_sesion:
       return jsonify({"success": False, "message": "Sesión no iniciada"}), 401

    user = usuario_service.obtener_usuario_por_nombre(nombre_sesion)
    
    if user:
        try:
            if user.orbes_rojos is None:
                user.orbes_rojos = 0
                
            user.orbes_rojos += 1000
            db.session.commit()
            return jsonify({"success": True, "new_total": user.orbes_rojos})
        except Exception as e:
            db.session.rollback()
            return jsonify({"success": False, "message": str(e)}), 500
        
    return jsonify({"success": False, "message": "Usuario no encontrado"}), 404