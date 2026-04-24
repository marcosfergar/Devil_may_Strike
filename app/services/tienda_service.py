from app.database.db import db
from app.models.schema import Usuario,Producto,Comentario

def obtener_productos_paginados(categoria='all', pagina=1, por_pagina=10):
    query = Producto.query
    
    if categoria != 'all':
        query = query.filter_by(categoria=categoria)
    
    return query.paginate(page=pagina, per_page=por_pagina, error_out=False)

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

def agregar_comentario(usuario_id, producto_id, texto):
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
        print(f"Error al crear comentario: {e}")
        return False

def obtener_producto_por_id(producto_id):
    return Producto.query.get(producto_id)