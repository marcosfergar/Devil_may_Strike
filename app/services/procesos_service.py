# app/services/procesos_service.py
from flask import session

def inject_vergil_status():
    user_id = session.get("user_id")
    if user_id:
        # Importación local para evitar importaciones circulares
        from app.services.inventario_service import tiene_tema_vergil
        return {'tiene_vergil_global': tiene_tema_vergil(user_id)}
    return {'tiene_vergil_global': False}