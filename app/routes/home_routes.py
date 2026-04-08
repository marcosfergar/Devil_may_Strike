from flask import Blueprint, redirect, render_template, session, url_for

# importe de rutas
# from app.routes.homeLogin_routes import homeLogin_pb

# importe modelos
# from app.models import trainer

# importe formularios
# from app.forms.trainer_form import TrainerForm

# importe sercicios
# from app.services.trainer_service import registrar_entrenador, autenticar_entrenador

home_pb = Blueprint('home_route', __name__, template_folder='templates')


@home_pb.route('/home', methods=['GET', 'POST'])
def paginaBienvenida():

    if "username" not in session:
            return redirect(url_for('home_login.paginaLogin'))
        
    return render_template('home.html', player=session.get("username"))


# @home_pb.route("/logout")
# def logout():
#     session.clear()
#     return redirect(url_for('homeLogin_route.paginaLogin'))