from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class TemaForm(FlaskForm):
    titulo = StringField('Título del Tema', validators=[DataRequired(), Length(max=100)])
    contenido = TextAreaField('Mensaje Inicial', validators=[DataRequired()])
    enviar = SubmitField('Forjar Tema')

class MensajeForm(FlaskForm):
    contenido = TextAreaField('Tu respuesta', validators=[DataRequired()])
    enviar = SubmitField('Responder')