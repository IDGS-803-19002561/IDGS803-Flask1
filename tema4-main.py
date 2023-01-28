
from flask import Flask
from flask import request 

app = Flask(__name__)


@app.route("/operasBas" , methods=['GET' , 'POST'])
def operasBas():
    if request.method == 'POST':
        num1=int(request.form.get('num1'))
        num2=int(request.form.get('num2'))
        return "La suma es : {}".format(num1 + num2)

    else :
        return ''' <form action="/operasBas" method="POST">
            <label for="">N1 :</label>  
            <input type="text" name="num1"> <br><br>
            <label for="">N2 :</label>
            <input type="text" name="num2"> <br><br>
            <label for="">Enviar</label>
            <input type="submit"  value="Enviar"> <br><br>
        </form> '''

if __name__ == '__main__':
    app.run(debug=True)