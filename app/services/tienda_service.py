from app.database.db import db
from app.models.schema import Usuario,Producto

def obtener_todos_los_productos():
    return Producto.query.all()

def comprar_producto(usuario_id, producto_id):
    usuario = Usuario.query.get(usuario_id)
    producto = Producto.query.get(producto_id)

    if not usuario or not producto:
        return {"success": False, "message": "Usuario o Producto no encontrado"}

    # 1. Validar si ya lo tiene
    if producto in usuario.productos:
        return {"success": False, "message": "Ya posees este artículo"}

    # 2. Validar si tiene suficientes orbes
    if usuario.orbes_rojos < producto.precio:
        return {"success": False, "message": "No tienes suficientes orbes rojos"}

    try:
        # 3. Lógica de intercambio
        usuario.orbes_rojos -= producto.precio
        usuario.productos.append(producto) # SQLAlchemy inserta en la tabla 'inventario'
        
        db.session.commit()
        return {"success": True, "message": f"¡{producto.nombre} desbloqueado! SSS"}
    except Exception as e:
        db.session.rollback()
        return {"success": False, "message": "Error en la transacción"}