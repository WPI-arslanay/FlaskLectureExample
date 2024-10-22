from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField 
from wtforms.validators import  ValidationError, DataRequired

class CourseNameForm(FlaskForm):
    name = StringField(label= "Please choose your class:", validators=[DataRequired()])
    submit = SubmitField('Submit')