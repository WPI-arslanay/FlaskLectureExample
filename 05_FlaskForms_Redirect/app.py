from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    if request.method == 'POST' and 'name' in request.form:
        name = request.form['name']
        return redirect(url_for('course',name=name))
    return render_template('index.html')

@app.route('/course/<name>')
def course(name):
    return render_template('course.html', name=name)
    
if __name__ == '__main__':
    app.run(debug=True)

