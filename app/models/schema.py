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
    password = Column(String(255), nullable=True)
    orbes_rojos = Column(Integer, default=1000)
    orbes_totales = Column(Integer, default=1000)
    is_guest = Column(db.Boolean, default=False)
    
    imagen_perfil = db.Column(db.String(200), default='default.png')
    titulo_actual = db.Column(db.String(100), default='Cazador Novato')

    # RELACIONES
    productos = db.relationship('Producto', secondary=inventario, backref='compradores')
    comentarios = db.relationship('Comentario', backref='autor_tienda', lazy=True)

    def __init__(self, nombre, password=None, is_guest=False):
        self.nombre = nombre
        self.is_guest = is_guest
        self.orbes_rojos = 1000
        if password:
            self.password = generate_password_hash(password)

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
    @property
    def url_avatar(self):
        if self.imagen_perfil == 'default.png':
            return "uploads/perfiles/default.png"
            
        from app.models.schema import Producto
        
        es_de_tienda = Producto.query.filter_by(data_path=self.imagen_perfil).first()
        
        if es_de_tienda:
            return f"uploads/tienda/{self.imagen_perfil}"
        
        return f"uploads/perfiles/{self.imagen_perfil}"
    
class Producto(db.Model):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    categoria = Column(String(50), nullable=False)
    precio = Column(Integer, nullable=False)
    data_path = Column(String(255))
    descripcion = Column(String(255))
    multiplicador = db.Column(db.Float, default=1.0)

    comentarios = db.relationship('Comentario', backref='producto_asociado', lazy=True)

# Tienda
class Comentario(db.Model):
    __tablename__ = "comentarios"
    id = Column(Integer, primary_key=True, autoincrement=True)
    contenido = Column(Text, nullable=False)
    fecha = Column(DateTime, default=datetime.utcnow)
    usuario_id = Column(Integer, db.ForeignKey('Usuarios.id'), nullable=False)
    producto_id = Column(Integer, db.ForeignKey('productos.id'), nullable=True)

# Foro
class Categoria(db.Model):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False, unique=True)
    descripcion = Column(String(255))

    temas = db.relationship('Tema', backref='categoria_asociada', lazy=True, cascade="all, delete-orphan")

class Tema(db.Model):
    __tablename__ = "temas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(100), nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    categoria_id = Column(Integer, db.ForeignKey('categorias.id'), nullable=False)
    usuario_id = Column(Integer, db.ForeignKey('Usuarios.id'), nullable=False)
    
    mensajes = db.relationship('Mensaje', backref='tema_asociado', lazy=True, cascade="all, delete-orphan")
    creador = db.relationship('Usuario', backref='temas_creados')

class Mensaje(db.Model):
    __tablename__ = "mensajes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    contenido = Column(Text, nullable=False)
    fecha_publicacion = Column(DateTime, default=datetime.utcnow)
    tema_id = Column(Integer, db.ForeignKey('temas.id'), nullable=False)
    usuario_id = Column(Integer, db.ForeignKey('Usuarios.id'), nullable=False)
    
    autor = db.relationship('Usuario', backref='mensajes_foro')