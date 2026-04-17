from flask import Blueprint, redirect, render_template, session, url_for, flash

# importe de rutas

# importe modelos
from app.models.schema import Usuario

# importe formularios

# importe sercicios
import app.services.inventario_service as inventario_service
import app.services.tienda_service as tienda_service
import app.services.usuario_service as usuario_service

tienda_bp = Blueprint('tienda_route', __name__, template_folder='templates')

@tienda_bp.route('/')
def ver_tienda():
    if "username" not in session:
        return redirect(url_for('homeLogin_route.paginaLogin'))
    lista_productos = tienda_service.obtener_todos_los_productos()

    nombre_sesion = session.get("username")
    user = usuario_service.obtener_usuario_por_nombre(nombre_sesion)

    return render_template('tienda.html', productos=lista_productos, usuario=user)

@tienda_bp.route('/comprar/<int:id>')
def comprar(id):
    user_id = session.get('user_id')
    resultado = inventario_service.comprar_producto(user_id, id)
    
    if resultado["success"]:
        flash(resultado["message"], "success")
    else:
        flash(resultado["message"], "error")
        
    return redirect(url_for('tienda_route.ver_tienda'))

