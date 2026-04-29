from app.repositories.usuario_repository import UsuarioRepository

def obtener_inventario_usuario(usuario_id):
    return UsuarioRepository.get_inventario(usuario_id)

def obtener_musica_desbloqueada(usuario_id):
    return UsuarioRepository.get_items_por_categoria(usuario_id, 'musica')

def obtener_titulos_desbloqueados(usuario_id):
    return UsuarioRepository.get_items_por_categoria(usuario_id, 'titulo')

def tiene_tema_vergil(usuario_id):
    productos = UsuarioRepository.get_items_por_categoria(usuario_id, 'tema')
    return any('dark slayer' in p.nombre.lower() for p in productos)