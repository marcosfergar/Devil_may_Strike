from app.models.schema import Producto, db

class ProductoRepository:
    @staticmethod
    def get_all():
        return Producto.query.all()

    @staticmethod
    def get_by_id(producto_id):
        return Producto.query.get(producto_id)

    @staticmethod
    def get_paginated(categoria='all', pagina=1, por_pagina=10):
        query = Producto.query
        if categoria != 'all':
            query = query.filter_by(categoria=categoria)
        return query.paginate(page=pagina, per_page=por_pagina, error_out=False)

    @staticmethod
    def registrar_compra(usuario, producto):
        """
        Realiza la transacción de compra: resta orbes y añade al inventario.
        Recibe los objetos de modelo ya cargados.
        """
        try:
            # 1. Modificamos los objetos (SQLAlchemy trackea estos cambios)
            usuario.orbes_rojos -= producto.precio
            usuario.productos.append(producto)
            
            # 2. Intentamos persistir ambos cambios en una sola transacción
            db.session.commit()
            return True
        except Exception as e:
            # Si algo falla (ej: conexión perdida), volvemos atrás
            db.session.rollback()
            print(f"Error crítico en la transacción de compra: {e}")
            return False