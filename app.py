from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'hola Mundo'

@app.route('/new/<usuario>')
def new(usuario):
    return 'hola {}'.format(usuario)

@app.route('/route')
def route():
    return 'route'