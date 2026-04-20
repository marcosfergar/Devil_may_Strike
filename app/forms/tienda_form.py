from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class ComentarioForm(FlaskForm):
    contenido = TextAreaField(
        "Deja tu reseña", 
        validators=[
            DataRequired(message="El comentario no puede estar vacío."),
            Length(max=255, message="El comentario es demasiado largo.")
        ]
    )
    enviar = SubmitField("Publicar Comentario")