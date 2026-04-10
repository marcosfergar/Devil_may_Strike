from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo

class PlayerForm(FlaskForm):
    player = StringField(
        "Nombre de Usuario",
        validators=[
            DataRequired(message="El campo no puede estar vacío."),
            Length(min=3, max=25, message="Debe tener entre 3 y 25 caracteres.")
        ]
    )

    passwd = PasswordField(
        "Contraseña",
        validators=[
            DataRequired(message="El campo no puede estar vacío."),
            Length(min=6, message="La contraseña debe ser más larga.") # Por seguridad
        ]
    )
    
    # Campo extra para registro
    confirm_passwd = PasswordField(
        "Repite la contraseña",
        validators=[
            DataRequired(message="Debes confirmar la contraseña."),
            EqualTo('passwd', message="Las contraseñas deben coincidir.")
        ]
    )

    enviar = SubmitField("Registrarse")

class LoginForm(FlaskForm):
    player = StringField(
        "Nombre de Usuario",
        validators=[DataRequired(message="Introduce tu nombre de cazador.")]
    )
    passwd = PasswordField(
        "Contraseña",
        validators=[DataRequired(message="La contraseña es obligatoria.")]
    )
    enviar = SubmitField("Iniciar Sesión")