from .cliente import Cliente

class ClientePremium(Cliente):
    tipo = "Premium"

    def __init__(self, nombre, apellido, correo, saldo, descuento):
        super().__init__(nombre, apellido, correo, saldo)
        self.descuento = descuento

    def comprar(self, monto):
        monto_desc = monto * (1 - self.descuento / 100)
        return super().comprar(monto_desc)
