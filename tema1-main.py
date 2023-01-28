from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, World - Tema 1!</p>"


if __name__ == '__main__':
    app.run(debug=True)