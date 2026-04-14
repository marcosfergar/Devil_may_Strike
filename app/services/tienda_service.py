from app.models.schema import Producto

def obtener_todos_los_productos():
    return Producto.query.all()