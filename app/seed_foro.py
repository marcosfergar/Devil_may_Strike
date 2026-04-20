from app import create_app
from app.database.db import db
from app.models.schema import Categoria

app = create_app()
with app.app_context():
    categorias = [
        Categoria(
            nombre="Estrategias de Combate", 
            descripcion="Comparte guías de combos, uso de armas y cómo derrotar a jefes en dificultad Dante Must Die."
        ),
        Categoria(
            nombre="Taberna General", 
            descripcion="Espacio para hablar de cualquier cosa relacionada con Devil May Strike o el mundo de DMC."
        ),
        Categoria(
            nombre="Reporte de Fallos (Bugs)", 
            descripcion="¿Has encontrado una brecha en la realidad? Infórmanos para que podamos parchear el Inframundo."
        )
    ]
    
    for cat in categorias:
        if not Categoria.query.filter_by(nombre=cat.nombre).first():
            db.session.add(cat)
    
    db.session.commit()
    print("Categorías forjadas: Estrategias, General y Bugs.")