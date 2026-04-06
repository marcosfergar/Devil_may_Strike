from flask import Blueprint, redirect, render_template, session, url_for

# importe de rutas
# from app.routes.pokedex_route import pokedex_pb

# importe modelos
# from app.models import trainer

# importe formularios
# from app.forms.trainer_form import TrainerForm

importe sercicios
# from app.services.trainer_service import registrar_entrenador, autenticar_entrenador

home_pb = Blueprint('home_route', __name__, template_folder='templates')


@home_pb.route('/', methods=['GET', 'POST'])
def paginaBienvenida():

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
    return render_template('index.html')


# @home_pb.route('/register', methods=['GET', 'POST'])
# def registro():

#     form = TrainerForm()

#     if form.validate_on_submit():

#         # Obtencion de los datos del usuario entrenador que añadio en el formulario.
#         nombreTrainer = form.trainer.data
#         passwdTrainer = form.passwd.data

#         entrenador = trainer(nombreTrainer, passwdTrainer)

#         # Recordar que la funcion crear_entrenador crear y retorna el objeto trainer, lo añade a la session y un commit en la bd.
#         registrar_entrenador(nombreTrainer, passwdTrainer)

#         session["trainer"] = entrenador.to_dict()

#         return redirect(url_for('batalla_route.PokedexS'))

#     return render_template('registro.html', form=form)


# @home_pb.route("/logout")
# def logout():
#     session.clear()
#     return redirect(url_for('home_route.Bienvenido'))