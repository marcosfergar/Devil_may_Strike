import os
from werkzeug.utils import secure_filename
from app.database.db import db
from app.models.schema import Usuario
from werkzeug.security import check_password_hash

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

def actualizar_ajustes_perfil(usuario, nueva_foto=None, nuevo_titulo=None):
    try:
        # Foto
        if nueva_foto:
            nombre_archivo = f"user_{usuario.id}_{secure_filename(nueva_foto.filename)}"
            ruta = os.path.join('app/static/uploads/perfiles', nombre_archivo)
            nueva_foto.save(ruta)
            usuario.imagen_perfil = nombre_archivo
        
        # Titutilo
        if nuevo_titulo:
            usuario.titulo_actual = nuevo_titulo
            
        db.session.commit()
        return True, "Perfil actualizado con éxito."
    except Exception as e:
        db.session.rollback()
        return False, f"Error, esto no chufla: {e}"