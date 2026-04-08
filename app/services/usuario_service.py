from app.database.db import db
from app.models.usuario import Usuario

def registrar_usuario(nombre, password_plano):

    existe = Usuario.query.filter_by(nombre=nombre).first()
    if existe:
        return False, "Ese nombre de cazador ya está ocupado."

    try:
        nuevo_usuario = Usuario(nombre=nombre, password=password_plano)
        
        db.session.add(nuevo_usuario)
        db.session.commit()
        return True, "Registro completado con éxito."
    
    except Exception as e:

        db.session.rollback()
        return False, f"Error en la base de datos: {str(e)}"