from app.database.db import db
from app.models.schema import Categoria, Tema, Mensaje, Usuario

def crear_nuevo_tema(usuario_id, categoria_id, titulo, contenido):
    """
    Crea un tema, su primer mensaje y recompensa al usuario.
    """
    try:
        # 1. Obtener al usuario para darle su recompensa
        user = Usuario.query.get(usuario_id)
        if not user:
            return None, "Usuario no encontrado."

        # 2. Crear el Tema (el contenedor)
        nuevo_tema = Tema(
            titulo=titulo,
            categoria_id=categoria_id,
            usuario_id=usuario_id
        )
        db.session.add(nuevo_tema)
        
        # Usamos flush para obtener el ID del tema antes del commit final
        db.session.flush() 

        # 3. Crear el primer Mensaje (el contenido del post)
        primer_mensaje = Mensaje(
            contenido=contenido,
            tema_id=nuevo_tema.id,
            usuario_id=usuario_id
        )
        db.session.add(primer_mensaje)

        recompensa = 50
        cat = Categoria.query.get(categoria_id)
        if cat and cat.nombre == "Reporte de Fallos (Bugs)":
            recompensa = 100 

        user.orbes_rojos += recompensa
        db.session.commit()
        return nuevo_tema, f"¡Tema forjado! +{recompensa} Orbes obtenidos."
        
    except Exception as e:
        db.session.rollback()
        print(f"Error al crear tema: {e}")
        return None, "Hubo un error en el inframundo al crear el tema."

def agregar_respuesta(usuario_id, tema_id, contenido):
    try:
        user = Usuario.query.get(usuario_id)
        if not user:
            return None, "Usuario no encontrado."

        nueva_respuesta = Mensaje(
            contenido=contenido,
            tema_id=tema_id,
            usuario_id=usuario_id
        )
        db.session.add(nueva_respuesta)

        user.orbes_rojos += 10
        
        db.session.commit()
        return nueva_respuesta, "Respuesta enviada. +10 Orbes obtenidos."
        
    except Exception as e:
        db.session.rollback()
        print(f"Error al responder: {e}")
        return None, "No se pudo enviar la respuesta al inframundo."

def obtener_mensajes_de_tema(tema_id):
    """Obtiene todos los mensajes de un tema específico"""
    return Mensaje.query.filter_by(tema_id=tema_id).order_by(Mensaje.fecha_publicacion.asc()).all()