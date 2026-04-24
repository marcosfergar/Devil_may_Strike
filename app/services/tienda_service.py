from app.repositories.producto_repository import ProductoRepository
from app.repositories.comentario_repository import ComentarioRepository
from app.repositories.usuario_repository import UsuarioRepository 
from app.database.db import db

def obtener_productos_paginados(categoria='all', pagina=1, por_pagina=10):
    return ProductoRepository.get_paginated(categoria, pagina)

def comprar_producto(usuario_id, producto_id):
    usuario = UsuarioRepository.get_by_id(usuario_id)
    producto = ProductoRepository.get_by_id(producto_id)

    if not usuario or not producto:
        return {"success": False, "message": "No encontrado"}

    if producto in usuario.productos:
        return {"success": False, "message": "Ya lo tienes"}

    if usuario.orbes_rojos < producto.precio:
        return {"success": False, "message": "Faltan orbes"}

    success = ProductoRepository.registrar_compra(usuario, producto)

    if success:
        return {"success": True, "message": "¡Adquirido! SSS"}
    else:
        return {"success": False, "message": "Error al procesar la compra"}

def agregar_comentario_producto(usuario_id, producto_id, texto):
    if not texto or len(texto.strip()) < 1:
        return False
    
    return ComentarioRepository.create(usuario_id, producto_id, texto)

def obtener_producto_por_id(producto_id):
    return ProductoRepository.get_by_id(producto_id)