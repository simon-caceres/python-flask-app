from flask import Flask, request, url_for, redirect, abort
from flask.templating import render_template
from pathlib import Path
import mysql.connector
# settings.py
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
midb = mysql.connector.connect(
    host='localhost',
    user= os.environ.get('DB_USERNAME'),
    password= os.environ.get('DB_PASSOWRD'),
    database= os.environ.get('DB_BASE')
)

cursor = midb.cursor(dictionary=True)

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
    cursor.execute('select * from usuarios')
    usuarios = cursor.fetchall()
    return render_template('route.html', usuarios = usuarios)

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', mensaje = "hola desde route")

@app.route('/crear', methods=['POST', 'GET'])
def crear():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        sql = 'insert into usuarios (username, email, nombre, apellido) values (%s, %s, %s, %s)'
        values = (username, email, nombre, apellido)
        cursor.execute(sql, values)
        midb.commit()
        return redirect(url_for('route'))

    return render_template('crear.html')