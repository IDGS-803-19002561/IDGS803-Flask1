
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Main"

@app.route("/hola")
def hola():
    return "<h1>Que onda desde Hola.py -  Tema 2!</h1>"


if __name__ == '__main__':
    app.run(debug=True)