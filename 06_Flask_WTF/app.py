from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField 
from wtforms.validators import  ValidationError, DataRequired
app = Flask(__name__)
app.config['SECRET_KEY'] =  'secret!'

class CourseNameForm(FlaskForm):
    name = StringField(label= "Please choose your class:", validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = CourseNameForm()
    if form.validate_on_submit():
        if form.name.data is not None:
            return redirect(url_for('course',name=form.name.data))
    return render_template('index.html',  form=form)

@app.route('/course/<name>')
def course(name):
    return render_template('course.html', name=name)
    
if __name__ == '__main__':
    app.run(debug=True)

