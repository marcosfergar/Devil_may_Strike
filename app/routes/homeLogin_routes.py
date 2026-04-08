from flask import Blueprint, redirect, render_template, session, url_for
import random

# importe de rutas
from app.routes.home_routes import home_pb

# importe modelos
# from app.models import trainer

# importe formularios
from app.forms.player_form import PlayerForm
from app.services.usuario_service import registrar_usuario

# importe sercicios
# from app.services.trainer_service import registrar_entrenador, autenticar_entrenador

homeLogin_pb = Blueprint('homeLogin_route', __name__, template_folder='templates')


@homeLogin_pb.route('/', methods=['GET', 'POST'])
def paginaLogin():

    # form = TrainerForm()
    # verifTrainer = None

    # if form.validate_on_submit():
    #     # Obtencion de los datos del usuario entrenador que añadido en el formulario.
    #     nombreTrainer = form.trainer.data
    #     passwdTrainer = form.passwd.data

    #     entrenador = trainer(nombreTrainer, passwdTrainer)

    #     verifTrainer = autenticar_entrenador(nombreTrainer, passwdTrainer)
    #     if verifTrainer == True:
    #         session["trainer"] = entrenador.to_dict()
    #         return redirect(url_for('batalla_route.PokedexS'))

    # return render_template('index.html', form=form, verifTrainer=verifTrainer)
    return render_template('home-login.html')

@homeLogin_pb.route('/invitado')
def iniciar_invitado():
    session.clear()
    numero_aleatorio = random.randint(1000, 9999)
    
    # Creacion guest
    session["user_id"] = numero_aleatorio
    session["username"] = f"Guest_Dante#{numero_aleatorio}"  # Nombre de usuario para el invitado
    session["is_guest"] = True
    
    return redirect(url_for('home_route.paginaBienvenida'))

@homeLogin_pb.route('/register', methods=['GET', 'POST'])
def registro():
    form = PlayerForm()
    
    if form.validate_on_submit():
        username = form.player.data
        password = form.passwd.data
        
        exito, mensaje = registrar_usuario(username, password)
        
        if exito:
            return redirect(url_for('homeLogin_route.paginaLogin'))
        else:
            return render_template('registro.html', form=form, error=mensaje)
        
    return render_template('registro.html', form=form)

# @home_pb.route("/logout")
# def logout():
#     session.clear()
#     return redirect(url_for('home_route.Bienvenido'))