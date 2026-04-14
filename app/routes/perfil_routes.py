from flask import Blueprint, redirect, render_template, session, url_for

# importe de rutas
# from app.routes.homeLogin_routes import homeLogin_pb

# importe modelos
# from app.models import trainer

# importe formularios
# from app.forms.trainer_form import TrainerForm

# importe sercicios
from app.services.rawg_service import listar_saga_dmc

perfil_pb = Blueprint('perfil_route', __name__, template_folder='templates')

@perfil_pb.route('/perfil', methods=['GET', 'POST'])
def perfil():
    if "username" not in session:
        return redirect(url_for('homeLogin_route.paginaLogin'))
    
    return render_template('perfil.html', player=session.get("username"))


