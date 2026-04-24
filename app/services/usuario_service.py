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
    if nuevo_titulo:
        usuario.titulo_actual = nuevo_titulo

    if foto_data:
        if foto_data.startswith('data:image'):
            format, imgstr = foto_data.split(';base64,') 
            ext = format.split('/')[-1]
            nombre_archivo = f"perfil_{usuario.id}_{int(datetime.utcnow().timestamp())}.{ext}"
            
            ruta = os.path.join('app/static/uploads/perfiles/', nombre_archivo)
            with open(ruta, "wb") as fh:
                fh.write(base64.b64decode(imgstr))
            
            usuario.imagen_perfil = nombre_archivo

        else:
            usuario.imagen_perfil = foto_data

    return UsuarioRepository.save(usuario)