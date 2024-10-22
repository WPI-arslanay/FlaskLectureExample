from flask_wtf import FlaskForm
from wtforms.fields import SelectField, StringField, SubmitField 
from wtforms.validators import  DataRequired

class CourseForm(FlaskForm):
    major = SelectField(label= "Please select major:", choices = ['CS', 'EE','MATH','ME', 'RBE'],validators=[DataRequired()])
    coursenum = StringField(label= "Please enter course number:", validators=[DataRequired()])
    title = StringField(label= "Please enter course title:", validators=[DataRequired()])
    submit = SubmitField('Submit')