from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError

class MiastoForm(FlaskForm):
	miasto = StringField('misato',validators=[DataRequired(),Length(min=2,max=40)])
	submit = SubmitField('Szukaj')
