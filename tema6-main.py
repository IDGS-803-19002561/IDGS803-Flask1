from flask import Flask, render_template
from flask import request 

app = Flask(__name__)

@app.route("/multiplicar")
def multiplicar():
    return render_template('multiplicar.html')

@app.route("/resultado" , methods=['POST'])
def resultado():
    num1=int(request.form.get('txtNum1'))
    num2=int(request.form.get('txtNum2'))
    res = num2 * num2
    return render_template('resultado.html', n1  = num1 , n2 = num2 , res = res)


if __name__ == '__main__':
    app.run(debug=True)