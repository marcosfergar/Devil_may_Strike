from flask import Blueprint, flash, jsonify, redirect, render_template, request, session, url_for

# importe sercicios
from app.services import usuario_service

perfil_pb = Blueprint('perfil_route', __name__, template_folder='templates')

@perfil_pb.route('/perfil', methods=['GET', 'POST'])
def perfil():
    if "username" not in session:
        return redirect(url_for('homeLogin_route.paginaLogin'))
    
    nombre_sesion = session.get("username")
    user = usuario_service.obtener_usuario_por_nombre(nombre_sesion)
    
    return render_template('perfil.html', usuario=user)

@perfil_pb.route('/actualizar', methods=['POST'])
def actualizar_perfil():
    nombre_sesion = session.get("username")
    user = usuario_service.obtener_usuario_por_nombre(nombre_sesion)
    
    if not user:
        return jsonify({"success": False, "message": "Sesión expirada"}), 401
    
    nuevo_titulo = request.form.get('titulo')
    foto_recortada_or_inventario = request.form.get('cropped_data')
    
    resultado = usuario_service.actualizar_perfil_completo(user, nuevo_titulo, foto_recortada_or_inventario)

    return jsonify(resultado)