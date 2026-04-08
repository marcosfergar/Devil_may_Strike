import os
from flask import Flask
from flask_session import Session

# importe database
from app.database.db import db

# importe de rutas
from app.routes.home_routes import home_pb
from app.routes.homeLogin_routes import homeLogin_pb


# importae modelos
from app.models.usuario import Usuario


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


# # Comando CLI
@app.cli.command("crear_tablas")
def crear_tablas():
    db.drop_all()
    print("Creando las tablas correspondientes para la base de datos ...")
    db.create_all()

    db.session.commit()
    print("Tablas creadas")


if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0', port=8080)
    app.run(host='127.0.0.1', port=5000, debug=True)