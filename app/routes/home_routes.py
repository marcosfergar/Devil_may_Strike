from flask import Blueprint, redirect, render_template, session, url_for
from flask import jsonify

# importe sercicios
from app.services import usuario_service, inventario_service
from app.services.rawg_service import listar_saga_dmc

home_pb = Blueprint('home_route', __name__, template_folder='templates')


@home_pb.route('/', methods=['GET', 'POST'])
def paginaBienvenida():
    user_id = session.get("user_id")
    
    if not user_id:
        return redirect(url_for('homeLogin_route.paginaLogin'))
    
    user = usuario_service.obtener_usuario_por_id(user_id)

    if not user:
        session.clear()
        return redirect(url_for('homeLogin_route.paginaLogin'))
    
    desbloqueado = inventario_service.tiene_tema_vergil(user_id)

    return render_template('home.html', usuario=user, tiene_vergil=desbloqueado)

@home_pb.route('/biblioteca-dmc')
def biblioteca_dmc():
    if "user_id" not in session:
            return redirect(url_for('homeLogin_route.paginaLogin'))
    
    nombre_sesion = session.get("username")
    user = usuario_service.obtener_usuario_por_nombre(nombre_sesion)

    juegos_saga = listar_saga_dmc()
    return render_template('biblioteca-dmc.html',usuario=user, juegos=juegos_saga)

@home_pb.route('/recompensa-tiempo', methods=['POST'])
def recompensa_tiempo():
    if "user_id" in session:
        user = usuario_service.obtener_usuario_por_id(session["user_id"])
        puntos_base = 10
        
        puntos_ganados = usuario_service.sumar_puntos_con_bonus(user, puntos_base)
        
        return {"success": True, "message": "puntos_ganados"}
    return {"success": False, "message": "Error al procesar la compra"}, 401

@home_pb.route('/mis-canciones')
def obtener_mis_canciones():
    user_id = session.get("user_id")
    if not user_id:
        return jsonify([])

    user = usuario_service.obtener_usuario_por_id(user_id)
    
    musica_comprada = [
        {
            "name": p.nombre,
            "src": f"/static/music/{p.data_path}"
        } 
        for p in user.productos if p.categoria.lower() == 'musica'
    ]
    
    return jsonify(musica_comprada)