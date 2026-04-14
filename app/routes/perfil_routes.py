from flask import Blueprint, redirect, render_template, session, url_for

# importe de rutas

# importe modelos

# importe formularios

# importe sercicios

perfil_pb = Blueprint('perfil_route', __name__, template_folder='templates')

@perfil_pb.route('/perfil', methods=['GET', 'POST'])
def perfil():
    if "username" not in session:
        return redirect(url_for('homeLogin_route.paginaLogin'))
    
    return render_template('perfil.html', player=session.get("username"))


