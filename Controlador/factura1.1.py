class Factura:
    __tasa = 18
    def __init__(self, unidad, precio):
        self.unidad = unidad
        self.precio = precio
    def por_pagar(self):
        total = self.unidad * self.precio
        impuesto = total * Factura.__tasa / 100
        return(total + impuesto)

compra1 = Factura(12, 110)
print(compra1.unidad)
print(compra1.precio)
print(compra1.por_pagar(), "Soles")
#print(Factura.__tasa)
