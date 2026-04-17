from app.database.db import db
from app.models.schema import Usuario, Producto

def obtener_inventario_usuario(usuario_id):
    usuario = Usuario.query.get(usuario_id)
    if usuario:
        # Esto accede a la relación 'productos' que definimos en el modelo
        return usuario.productos 
    return []

    
def obtener_musica_desbloqueada(usuario_id):
    usuario = Usuario.query.get(usuario_id)
    musica = [p for p in usuario.productos if p.categoria == 'musica']
    return musica

def obtener_titulos_desbloqueados(usuario_id):
    usuario = Usuario.query.get(usuario_id)
    return [p for p in usuario.productos if p.categoria == 'titulo']

def tiene_tema_vergil(usuario_id):
    usuario = Usuario.query.get(usuario_id)
    return any(p.categoria == 'tema' and 'vergil' in p.nombre.lower() for p in usuario.productos)