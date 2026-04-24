from app.models.schema import Tema, Mensaje, Categoria, db

class ForoRepository:
    @staticmethod
    def get_all_categorias():
        return Categoria.query.all()
    
    @staticmethod
    def get_categorias_by_id(categoria_id):
        return Categoria.query.get(categoria_id)
    
    @staticmethod
    def get_temas_by_categoria(categoria_id):
        return Tema.query.filter_by(categoria_id=categoria_id).order_by(Tema.fecha_creacion.desc()).all()
    
    @staticmethod
    def get_tema_by_id(tema_id):
        return Tema.query.get(tema_id)

    @staticmethod
    def crear_tema_completo(usuario, categoria_id, titulo, contenido, recompensa):
        try:
            nuevo_tema = Tema(
                titulo=titulo,
                categoria_id=categoria_id,
                usuario_id=usuario.id
            )
            db.session.add(nuevo_tema)
            db.session.flush()

            primer_mensaje = Mensaje(
                contenido=contenido,
                tema_id=nuevo_tema.id,
                usuario_id=usuario.id
            )
            db.session.add(primer_mensaje)

            usuario.orbes_rojos += recompensa
            
            db.session.commit()
            return nuevo_tema
        except Exception as e:
            db.session.rollback()
            print(f"Error en ForoRepository (Tema): {e}")
            return None

    @staticmethod
    def crear_respuesta(usuario, tema_id, contenido, recompensa):
        try:
            nueva_respuesta = Mensaje(
                contenido=contenido,
                tema_id=tema_id,
                usuario_id=usuario.id
            )
            db.session.add(nueva_respuesta)
            usuario.orbes_rojos += recompensa
            usuario.orbes_totales += recompensa
            
            db.session.commit()
            return nueva_respuesta
        except Exception as e:
            db.session.rollback()
            print(f"Error en ForoRepository (Respuesta): {e}")
            return None

    @staticmethod
    def get_mensajes_by_tema(tema_id):
        return Mensaje.query.filter_by(tema_id=tema_id).order_by(Mensaje.fecha_publicacion.asc()).all()
    @staticmethod
    def get_categoria_by_id(categoria_id):
        return Categoria.query.get(categoria_id)