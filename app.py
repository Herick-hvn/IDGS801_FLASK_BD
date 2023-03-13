from flask import Flask, render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import jsonify

from teachers.routes import teachers

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['GET'])
def home():
    return jsonify({'Datos':'Hola'})

app.register_blueprint(teachers)

if __name__ == '__main__':
    app.run()