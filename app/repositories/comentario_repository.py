from app.models.schema import Comentario, db

class ComentarioRepository:
    @staticmethod
    def create(usuario_id, producto_id, texto):
        try:
            nuevo = Comentario(
                contenido=texto,
                usuario_id=usuario_id,
                producto_id=producto_id
            )
            db.session.add(nuevo)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error en ComentarioRepository: {e}")
            return False