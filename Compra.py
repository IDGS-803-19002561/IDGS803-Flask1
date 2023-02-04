
class Compra:
    boletos = 0
    descuento = 0

    def setBoletos(self, a):
        self.boletos = a

    def getBoleto(self):
        return self.boletos


    def setDesc(self, a):
        self.descuento = a

    def getDes(self):
        return self.descuento

    def main(self) :
        totalPago = self.boletos * 12
        descuento = 0
        if(self.boletos > 5 ):
            descuento = totalPago * 0.15
        elif(self.boletos >= 3 and self.boletos <= 5) :
            descuento = totalPago * 0.10

        self.setDesc(descuento)

        return totalPago - descuento

