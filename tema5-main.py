from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    nombre = 'Filemona'
    lista1 = ['Español' , 'Ingles' , 'Quimica']
    return render_template('index.html' , name=nombre , list=lista1)


@app.route("/usuarios")
def usaurios():
    lista1 = ['Español' , 'Ingles' , 'Quimica']
    return render_template('archivo2.html', list=lista1)

    

if __name__ == '__main__':
    app.run(debug=True)