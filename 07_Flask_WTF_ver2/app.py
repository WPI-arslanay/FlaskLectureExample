from flask import Flask, render_template, request, redirect, url_for
from forms import CourseNameForm

app = Flask(__name__)
app.config['SECRET_KEY'] =  'secret!'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = CourseNameForm()
    if form.validate_on_submit():
        if form.name.data is not None:
            return redirect(url_for('course',name=form.name.data))
    return render_template('index.html', form=form)

@app.route('/course/<name>')
def course(name):
    return render_template('course.html', name=name)
    
if __name__ == '__main__':
    app.run(debug=True)

