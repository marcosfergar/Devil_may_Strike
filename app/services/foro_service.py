from app.repositories.foro_repository import ForoRepository
from app.repositories.usuario_repository import UsuarioRepository

def crear_nuevo_tema(usuario_id, categoria_id, titulo, contenido):
    user = UsuarioRepository.get_by_id(usuario_id)
    if not user:
        return None, "Usuario no encontrado."

    recompensa = 50
    cat = ForoRepository.get_categoria_by_id(categoria_id)
    if cat and cat.nombre == "Reporte de Fallos (Bugs)":
        recompensa = 100 

    tema = ForoRepository.crear_tema_completo(user, categoria_id, titulo, contenido, recompensa)
    
    if tema:
        return tema, f"¡Tema creado! +{recompensa} Orbes obtenidos."
    return None, "Hubo un error al crear el tema."

def agregar_respuesta(usuario_id, tema_id, contenido):
    user = UsuarioRepository.get_by_id(usuario_id)
    if not user:
        return None, "Usuario no encontrado."

    recompensa = 10
    
    respuesta = ForoRepository.crear_respuesta(user, tema_id, contenido, recompensa)
    
    if respuesta:
        return respuesta, "Respuesta enviada. +10 Orbes obtenidos."
    return None, "No se pudo enviar la respuesta."

def obtener_categoria_por_id(categoria_id):
    return ForoRepository.get_categorias_by_id(categoria_id)

def obtener_todas_las_categorias():
    return ForoRepository.get_all_categorias()

def obtener_temas_por_categoria(categoria_id):
    return ForoRepository.get_temas_by_categoria(categoria_id)

def obtener_tema_por_id(tema_id):
    return ForoRepository.get_tema_by_id(tema_id)

def obtener_mensajes_de_tema(tema_id):
    return ForoRepository.get_mensajes_by_tema(tema_id)