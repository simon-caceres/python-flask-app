from flask import Flask, request, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return 'hola Mundo'

@app.route('/post/<post_id>', methods=['GET'])
def get_post(post_id):
    return 'el id del post es: {}'.format(post_id)

@app.route('/post/<post_id>', methods=['POST'])
def post_post(post_id):
    return 'el id del post es: {}'.format(post_id)

@app.route('/route', methods=['POST'])
def route():
    print(url_for('post_post', post_id = 2))
    print(request.form['llave1'])
    print(request.form['llave2'])
    return 'recibimos tus datos'