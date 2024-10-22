from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello!</h1>"

@app.route('/course')
def course():
	return '<h1>Hello class!</h1>'

@app.route('/course/<string:name>')
def mycourse(name):
	return '<h1>Hello, {0} class!</h1>'.format(name)

@app.route('/appname')
def appname():
    return "<h1>Application name:{}</h1>".format(__name__)

if __name__ == '__main__':
    app.run(debug=True)

