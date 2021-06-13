from flask import Flask, request, url_for, redirect, abort
from flask.templating import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'hola Mundo'

@app.route('/post/<post_id>', methods=['POST', 'GET'])
def get_post(post_id):
    if request.method == 'GET':
        return 'el id del post es: {}'.format(post_id)
    else:
        return {
            "username": "user",
            "email": "email.com"
        }


@app.route('/route', methods=['POST', 'GET'])
def route():
    #abort(403)
    #return redirect(url_for('get_post', post_id = 2))
    # print(request.form['llave1'])
    # print(request.form['llave2'])
    return render_template('route.html')

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', mensaje = "hola desde route")