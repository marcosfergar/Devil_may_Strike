from flask import Blueprint, redirect, render_template, session, url_for, flash
import random

# importe de rutas
from app.database import db
from app.routes.home_routes import home_pb

# importe modelos

# importe formularios
from app.forms.usuario_form import UsuarioForm, LoginForm

# importe sercicios
from app.services import usuario_service
from app.services.usuario_service import registrar_usuario, verificar_usuario

homeLogin_pb = Blueprint('homeLogin_route', __name__, template_folder='templates')

@homeLogin_pb.route('/')
def index():
    return render_template('home-login.html')

@homeLogin_pb.route('/login', methods=['GET', 'POST'])
def paginaLogin():
    form = LoginForm()
    
    if form.validate_on_submit():
        username = form.usuario.data
        password = form.passwd.data
        exito, resultado = verificar_usuario(username, password)
        
        if exito:
            session['user_id'] = resultado.id
            session['username'] = resultado.nombre
            return redirect(url_for('home_route.paginaBienvenida'))
        else:
            flash("Tu usuario o contraseña son incorrectos", "error")            
    return render_template('login.html', form=form)
            
@homeLogin_pb.route('/invitado')
def iniciar_invitado():
    session.clear()
    numero_aleatorio = random.randint(1000, 9999)
    nombre_temp = f"Guest_Dante#{numero_aleatorio}"
    
    invitado_db = usuario_service.crear_usuario_invitado(nombre_temp)
    
    if invitado_db:
        session["user_id"] = invitado_db.id 
        session["username"] = invitado_db.nombre
        session["is_guest"] = True
        return redirect(url_for('home_route.paginaBienvenida'))
    else:
        return "Error al forjar la identidad del invitado", 500

@homeLogin_pb.route('/register', methods=['GET', 'POST'])
def registro():
    form = UsuarioForm()
    
    if form.validate_on_submit():
        username = form.usuario.data
        password = form.passwd.data
        
        exito, mensaje = registrar_usuario(username, password)
        
        if exito:
            session['username'] = username
            return redirect(url_for('home_route.paginaBienvenida'))
        else:
            return render_template('registro.html', form=form, error=mensaje)
        
    return render_template('registro.html', form=form)

@homeLogin_pb.route('/logout')
def logout():
    user_id = session.get("user_id")
    
    usuario_service.gestionar_cierre_sesion(user_id)

    session.clear()
    
    return redirect(url_for('home_route.paginaBienvenida'))