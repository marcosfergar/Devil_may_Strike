from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length


class PlayerForm(FlaskForm):
    player = StringField(
        "Introduce el nombre del usuario",
        validators=[
            DataRequired(message="El campo no puede estar vacío."),
            Length(min=3, max=25, message="Debe tener entre 3 y 25 caracteres.")
        ]
    )

    passwd = PasswordField(
        "Introduce la contraseña del usuario",
        validators=[
            DataRequired(message="El campo no puede estar vacío.")
        ]
    )
    enviar = SubmitField("Enviar")