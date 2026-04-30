from datetime import datetime
import os
import base64
from werkzeug.security import check_password_hash
from app.repositories.usuario_repository import UsuarioRepository

# LOGIN Y MOVIDAS DE ESAS
def obtener_usuario_por_nombre(nombre):    
    return UsuarioRepository.get_by_nombre(nombre)

def obtener_usuario_por_id(usuario_id):
    return UsuarioRepository.get_by_id(usuario_id)

def registrar_usuario(nombre, password_plano):
    existe = UsuarioRepository.get_by_nombre(nombre)
    if existe:
        return False, "Ese nombre de usuario ya está usado."

    nuevo_usuario = UsuarioRepository.create(nombre=nombre, password=password_plano, is_guest=False)

    if nuevo_usuario:
        return True, "Registro completado con éxito."
    return False, "Error al acceder a la base de datos."
    
def crear_usuario_invitado(nombre_invitado):
    return UsuarioRepository.create(
            nombre=nombre_invitado, 
            password=None, 
            is_guest=True
        )

def verificar_usuario(nombre, password_plano):
    usuario = UsuarioRepository.get_by_nombre(nombre)
    
    if usuario and usuario.password:
        if check_password_hash(usuario.password, password_plano):
            return True, usuario
        else:
            print(f"Intento de login fallido para: {nombre} (Contraseña incorrecta)")
    
    return False, "Nombre o contraseña incorrectos."

def gestionar_cierre_sesion(user_id):
    user = UsuarioRepository.get_by_id(user_id)
    if user and user.is_guest:
        return UsuarioRepository.delete(user)
    return False

# PAL PERFIL

def actualizar_perfil_completo(usuario, nuevo_titulo, foto_data):
    try:
        if nuevo_titulo:
            usuario.titulo_actual = nuevo_titulo

        if foto_data:
            if foto_data.startswith('data:image'):
                import base64, os, glob
                format, imgstr = foto_data.split(';base64,') 
                ext = format.split('/')[-1]
                
                nombre_base = f"perfil_{usuario.id}"
                nombre_archivo = f"{nombre_base}.{ext}"
                directorio = 'app/static/uploads/perfiles/'
                
                if not os.path.exists(directorio):
                    os.makedirs(directorio)

                # Limpiar archivos viejos para evitar duplicados .png/.jpg
                for archivo_viejo in glob.glob(os.path.join(directorio, f"{nombre_base}.*")):
                    os.remove(archivo_viejo)
                
                ruta = os.path.join(directorio, nombre_archivo)
                with open(ruta, "wb") as fh:
                    fh.write(base64.b64decode(imgstr))
                
                usuario.imagen_perfil = nombre_archivo
            else:
                # Si viene del inventario
                usuario.imagen_perfil = foto_data

        exito = UsuarioRepository.save(usuario)
        
        if exito:
            return {
                "success": True, 
                "message": "¡Identidad actualizada, cazador!",
                "nueva_imagen": usuario.imagen_perfil
            }
        return {"success": False, "message": "Error al guardar en la base de datos."}

    except Exception as e:
        print(f"Error en actualizar_perfil: {e}")
        return {"success": False, "message": str(e)}

def dar_orbes_truco(usuario_id, cantidad=1000):
    return UsuarioRepository.sumar_orbes_truco(usuario_id, cantidad)

def obtener_ranking_usuarios(limite=5):
    return UsuarioRepository.get_top_ricos(limite)

# app/services/usuario_service.py

def obtener_multiplicador_total(usuario_id):
    multiplicador_total = 1.0
    objetos = UsuarioRepository.get_items_por_categoria(usuario_id, 'objeto')
    for obj in objetos:
        if obj.multiplicador:
            multiplicador_total += (obj.multiplicador - 1.0)
    
    return round(multiplicador_total, 2)

def sumar_puntos_con_bonus(usuario_id, puntos_base):
    bonus = obtener_multiplicador_total(usuario_id) 
    
    puntos_finales = int(puntos_base * bonus)
    
    UsuarioRepository.actualizar_orbes(usuario_id, puntos_finales)
    
    return puntos_finales