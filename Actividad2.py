from flask import Flask, render_template
from flask import request 
from Compra import Compra

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('cinepolis.html')

@app.route("/comprar" , methods=['POST'])
def comprar():
    nombre= request.form.get('txtNombre')
    pago=float(request.form.get('txtTipoPago'))
    
    objCompra = Compra()
    objCompra.setBoletos(int(request.form.get('txtBoletos')));
    subtotal = objCompra.getBoleto() * 12;
    
    totalPago = objCompra.main()
    if(pago == 2) :
        totalPago = totalPago * 0.90
        print(totalPago)

    return render_template('cineres.html' , nombre = nombre,subtotal = subtotal, boletos = objCompra.getBoleto() , descuento = objCompra.getDes(), total = totalPago , Tpago = pago)


if __name__ == '__main__':
    app.run(debug=True)