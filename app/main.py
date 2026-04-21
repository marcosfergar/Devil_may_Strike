import os,json
from flask import Flask
from flask_session import Session

# importe database
from app.database.db import db

# importe de rutas
from app.routes.home_routes import home_pb
from app.routes.homeLogin_routes import homeLogin_pb
from app.routes.perfil_routes import perfil_pb
from app.routes.tienda_routes import tienda_bp
from app.routes.foro_routes import foro_bp


# importae modelos
from app.models.schema import Categoria, Usuario, Producto, Comentario

app = Flask(__name__, template_folder='templates')
app.secret_key = "DevilStrike3"

# Configuracion session
app.config["SESSION_TYPE"] = "filesystem"   # Guardar en ficheros
app.config["SESSION_PERMANENT"] = False     # Sesiones temporales
app.config["SESSION_FILE_DIR"] = "./.flask_session"  # Carpeta donde se guardan

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
BD_PATH = os.path.join(BASE_DIR, "jugadores.db")

# # Configuracion alchemy
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{BD_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False




# Inicializar la extensión
Session(app)
db.init_app(app)

# Rutas
app.register_blueprint(homeLogin_pb, url_prefix='/')
app.register_blueprint(home_pb, url_prefix='/home')
app.register_blueprint(perfil_pb, url_prefix='/perfil')
app.register_blueprint(tienda_bp, url_prefix='/tienda')
app.register_blueprint(foro_bp, url_prefix='/foro')



# # Comando CLI
def seed_categorias():
    """Función auxiliar para insertar categorías iniciales"""
    # Lista de categorías para iterar fácilmente
    categorias_data = [
        {"nombre": "Estrategias de Combate", "descripcion": "Guías para rango SSS."},
        {"nombre": "Taberna General", "descripcion": "Charla general de cazadores."},
        {"nombre": "Reporte de Bugs", "descripcion": "Inestabilidad en el inframundo."}
    ]
    
    for cat in categorias_data:
        # Esto evita que el script falle si la categoría ya existe
        existe = Categoria.query.filter_by(nombre=cat['nombre']).first()
        if not existe:
            nueva_cat = Categoria(nombre=cat['nombre'], descripcion=cat['descripcion'])
            db.session.add(nueva_cat)
    
    db.session.commit()
    print("¡Categorías forjadas con éxito!")

@app.cli.command("crear_tablas")
def crear_tablas():
    db.drop_all()
    print("Borrando tablas antiguas...")
    db.create_all()
    print("Tablas creadas con éxito.")
    
    # 1. Cargar Productos desde JSON
    json_path = os.path.join(app.root_path, 'data', 'productos.json')
    if os.path.exists(json_path):
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                productos_data = json.load(f)
            
            for p in productos_data:
                nuevo_producto = Producto(
                    nombre=p['nombre'],
                    categoria=p['tipo'],
                    precio=p['precio'],
                    descripcion=p.get('descripcion', ''),
                    data_path=p.get('imagen_url', 'default_item.png')
                )
                db.session.add(nuevo_producto)
            
            db.session.commit()
            print(f"Tienda cargada: {len(productos_data)} items forjados.")
        except Exception as e:
            db.session.rollback()
            print(f"Error crítico al cargar JSON: {e}")
    
    # 2. Cargar Categorías del Foro
    try:
        seed_categorias()
    except Exception as e:
        print(f"Error al insertar categorías: {e}")

    print("--- PROCESO FINALIZADO: RANGO SSS ---")

if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0', port=8080)
    app.run(host='127.0.0.1', port=5000, debug=True)