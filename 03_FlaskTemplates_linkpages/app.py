from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/course/<name>')
def course(name):
    return render_template('course.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)

