from datetime import datetime
import os
import base64
import time
from flask import current_app
from app.database.db import db
from app.models.schema import Usuario
from werkzeug.security import check_password_hash

# LOGIN Y MOVIDAS DE ESAS
def obtener_usuario_por_nombre(nombre):
    if not nombre:
        return None
        
    return Usuario.query.filter_by(nombre=nombre).first()

def obtener_usuario_por_id(usuario_id):
    
    return Usuario.query.get(usuario_id)

def registrar_usuario(nombre, password_plano):

    existe = Usuario.query.filter_by(nombre=nombre).first()
    if existe:
        return False, "Ese nombre de usuario ya está usado."

    try:
        nuevo_usuario = Usuario(nombre=nombre, password=password_plano, is_guest=False)
        db.session.add(nuevo_usuario)
        db.session.commit()
        return True, "Registro completado con éxito."
    except Exception as e:
        db.session.rollback()
        return False, str(e)
    
def crear_usuario_invitado(nombre_invitado):
    try:
        nuevo_invitado = Usuario(
            nombre=nombre_invitado, 
            password=None, 
            is_guest=True
        )
        db.session.add(nuevo_invitado)
        db.session.commit()
        return nuevo_invitado
    except Exception as e:
        db.session.rollback()
        return None

def verificar_usuario(nombre, password_plano):
    usuario = Usuario.query.filter_by(nombre=nombre).first()
    
    if usuario:
        if check_password_hash(usuario.password, password_plano):
            return True, usuario
        else:
            print("la contraseña ta mal")
    
    return False, "Nombre o contraseña incorrectos."

def gestionar_cierre_sesion(user_id):
    if not user_id:
        return False
        
    try:
        user = Usuario.query.get(user_id)
        if user and user.is_guest:
            db.session.delete(user)
            db.session.commit()
            return True
    except Exception as e:
        db.session.rollback()
        print(f"Error al eliminar invitado durante logout: {e}")
        
    return False

# PAL PERFIL

def actualizar_perfil_completo(usuario, nuevo_titulo, foto_data):
    if nuevo_titulo:
        usuario.titulo_actual = nuevo_titulo

    if foto_data:
        if foto_data.startswith('data:image'):
            format, imgstr = foto_data.split(';base64,') 
            ext = format.split('/')[-1]
            nombre_archivo = f"perfil_{usuario.id}_{int(datetime.utcnow().timestamp())}.{ext}"
            
            ruta = os.path.join('app/static/uploads/perfiles/', nombre_archivo)
            with open(ruta, "wb") as fh:
                fh.write(base64.b64decode(imgstr))
            
            usuario.imagen_perfil = nombre_archivo

        else:
            usuario.imagen_perfil = foto_data

    db.session.commit()