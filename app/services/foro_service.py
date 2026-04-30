from app.repositories.foro_repository import ForoRepository
from app.repositories.usuario_repository import UsuarioRepository

def crear_nuevo_tema(usuario_id, categoria_id, titulo, contenido):
    user = UsuarioRepository.get_by_id(usuario_id)
    if not user:
        return None, "Usuario no encontrado."

    # recompensa normla
    recompensa_base = 50
    cat = ForoRepository.get_categoria_by_id(categoria_id)
    if cat and cat.nombre == "Reporte de Fallos (Bugs)":
        recompensa_base = 100 

    # Bonus
    from app.services import usuario_service
    bonus = usuario_service.obtener_multiplicador_total(user.id)
    recompensa_final = int(recompensa_base * bonus)

    tema = ForoRepository.crear_tema_completo(user, categoria_id, titulo, contenido, recompensa_final)
    
    if tema:
        return tema, {
            "puntos": recompensa_final,
            "texto": f"¡Tema creado! +{recompensa_final} Orbes obtenidos.",
            "categoria": "success"
        }
    return None, {"texto": "Hubo un error", "categoria": "error"}

def agregar_respuesta(usuario_id, tema_id, contenido):
    user = UsuarioRepository.get_by_id(usuario_id)
    if not user:
        return None, {"texto": "Usuario no encontrado.", "categoria": "error"}

    recompensa_base = 10
    
    # Bonus
    from app.services import usuario_service
    bonus = usuario_service.obtener_multiplicador_total(user.id)
    recompensa_final = int(recompensa_base * bonus)
    
    respuesta = ForoRepository.crear_respuesta(user, tema_id, contenido, recompensa_final)
    
    if respuesta:
        return respuesta, {
            "puntos": recompensa_final,
            "texto": f"Respuesta enviada. +{recompensa_final} Orbes obtenidos.",
            "categoria": "success",
        }
    return None, {"texto": "No se pudo enviar la respuesta.", "categoria": "error"}

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