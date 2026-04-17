from sqlalchemy import Column, Integer, String, ForeignKey, Table, Text, DateTime
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from app.database.db import db
from datetime import datetime

# Tabla Inventario
inventario = db.Table('inventario',
    db.Column('usuario_id', db.Integer, db.ForeignKey('Usuarios.id'), primary_key=True),
    db.Column('producto_id', db.Integer, db.ForeignKey('productos.id'), primary_key=True),
    db.Column('fecha_compra', db.DateTime, default=datetime.utcnow)
)

class Usuario(db.Model):
    __tablename__ = "Usuarios"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    orbes_rojos = Column(Integer, default=1000)

    # RELACIONES
    productos = db.relationship('Producto', secondary=inventario, backref='compradores')
    comentarios = db.relationship('Comentario', backref='autor', lazy=True)

    def __init__(self, nombre, password, id=None):
        self.id = id
        self.nombre = nombre
        self.password = generate_password_hash(password)
        self.orbes_rojos = 1000

    def set_password(self, newPassword):
        self.password = generate_password_hash(newPassword)

    def verificar_password(self, passwd):
        return check_password_hash(self.password, passwd)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "orbes_rojos": self.orbes_rojos
        }

class Producto(db.Model):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    categoria = Column(String(50), nullable=False) # 'musica', 'avatar', 'titulo', 'tema'
    precio = Column(Integer, nullable=False)
    data_path = Column(String(255))
    descripcion = Column(String(255))

    # RELACIÓN
    comentarios = db.relationship('Comentario', backref='producto_asociado', lazy=True)

class Comentario(db.Model):
    __tablename__ = "comentarios"
    id = Column(Integer, primary_key=True, autoincrement=True)
    contenido = Column(Text, nullable=False)
    fecha = Column(DateTime, default=datetime.utcnow)

    # CLAVES FORÁNEAS
    usuario_id = Column(Integer, db.ForeignKey('Usuarios.id'), nullable=False)
    producto_id = Column(Integer, db.ForeignKey('productos.id'), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "contenido": self.contenido,
            "autor": self.autor.nombre,
            "fecha": self.fecha.strftime("%Y-%m-%d %H:%M:%S")
        }