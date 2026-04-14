from flask import Blueprint, redirect, render_template, session, url_for, flash

# importe de rutas

# importe modelos

# importe formularios

# importe sercicios
import app.services.inventario_service as inventario_service

tienda_bp = Blueprint('tienda_route', __name__, template_folder='templates')

@tienda_bp.route('/')
def ver_tienda():
    if "username" not in session:
        return redirect(url_for('homeLogin_route.paginaLogin'))
    
    return render_template('tienda.html', player=session.get("username"))

@tienda_bp.route('/comprar/<int:id>')
def comprar(id):
    user_id = session.get('user_id')
    resultado = inventario_service.comprar_producto(user_id, id)
    
    if resultado["success"]:
        flash(resultado["message"], "success")
    else:
        flash(resultado["message"], "error")
        
    return redirect(url_for('tienda.ver_tienda'))

