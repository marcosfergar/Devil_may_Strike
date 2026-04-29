from app.models.schema import Usuario, db

class UsuarioRepository:
    @staticmethod
    def get_by_id(usuario_id):
        return Usuario.query.get(usuario_id)

    @staticmethod
    def get_by_nombre(nombre):
        return Usuario.query.filter_by(nombre=nombre).first()
    
    @staticmethod
    def create(nombre, password=None, is_guest=False):
        try:
            nuevo_usuario = Usuario(
                nombre=nombre,
                password=password,
                is_guest=is_guest
            )
            db.session.add(nuevo_usuario)
            db.session.commit()
            return nuevo_usuario
        except Exception as e:
            db.session.rollback()
            print(f"Error en UsuarioRepository al crear: {e}")
            return None
        
    @staticmethod
    def save(usuario):
        try:
            db.session.add(usuario)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error al guardar usuario: {e}")
            return False

    @staticmethod
    def delete(usuario):
        try:
            db.session.delete(usuario)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False
        
    @staticmethod
    def get_top_ricos(limite=5):
        return Usuario.query.filter_by(is_guest=False)\
                            .order_by(Usuario.orbes_totales.desc())\
                            .limit(limite).all()
    
    @staticmethod
    def get_inventario(usuario_id):
        usuario = Usuario.query.get(usuario_id)
        return usuario.productos if usuario else []

    @staticmethod
    def get_items_por_categoria(usuario_id, categoria):
        usuario = Usuario.query.get(usuario_id)
        if not usuario:
            return []
        return [p for p in usuario.productos if p.categoria == categoria]
    
    def actualizar_orbes(usuario_id, orbes_a_sumar):
        user = Usuario.query.get(usuario_id)
        if user:
            user.orbes += orbes_a_sumar
            db.session.commit() 
            return user.orbes
        
        return None

    @staticmethod
    def sumar_orbes_truco(usuario_id, cantidad):
        from app.models.schema import Usuario, db
        try:
            usuario = Usuario.query.get(usuario_id)
            if usuario:
                usuario.orbes_rojos = (usuario.orbes_rojos or 0) + cantidad
                usuario.orbes_totales = (usuario.orbes_totales or 0) + cantidad
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            print(f"Error en UsuarioRepository (truco): {e}")
            return False