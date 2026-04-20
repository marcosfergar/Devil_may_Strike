from flask import Blueprint, render_template, session, redirect, url_for, flash
from app.models.schema import Categoria, Tema
from app.services import foro_service, usuario_service
from app.forms.foro_form import TemaForm, MensajeForm # Los crearemos en el paso 3

foro_bp = Blueprint('foro_route', __name__, template_folder='templates')

@foro_bp.route('/')
def index_foro():
    user = usuario_service.obtener_usuario_por_id(session.get("user_id"))
    categorias = Categoria.query.all()
    return render_template('foro.html', categorias=categorias, usuario=user)

@foro_bp.route('/categoria/<int:id>')
def ver_categoria(id):
    categoria = Categoria.query.get_or_404(id)
    user = usuario_service.obtener_usuario_por_id(session.get("user_id"))
    return render_template('foro/categoria.html', categoria=categoria, usuario=user)

@foro_bp.route('/tema/<int:id>', methods=['GET', 'POST'])
def ver_tema(id):
    tema = Tema.query.get_or_404(id)
    user = usuario_service.obtener_usuario_por_id(session.get("user_id"))
    form = MensajeForm() # Para poder responder dentro del tema
    return render_template('foro/tema.html', tema=tema, usuario=user, form=form)