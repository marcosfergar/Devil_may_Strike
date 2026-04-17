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
        nuevo_usuario = Usuario(nombre=nombre, password=password_plano)
        
        db.session.add(nuevo_usuario)
        db.session.commit()
        return True, "Registro completado con éxito."
    
    except Exception as e:
        db.session.rollback()
        return False, f"Error en la base de datos: {str(e)}"

def verificar_usuario(nombre, password_plano):
    usuario = Usuario.query.filter_by(nombre=nombre).first()
    
    if usuario:
        if check_password_hash(usuario.password, password_plano):
            return True, usuario
        else:
            print("la contraseña ta mal")
    
    return False, "Nombre o contraseña incorrectos."