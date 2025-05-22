class Cliente:
    tipo = "Regular"

    def __init__(self, nombre, apellido, correo, saldo):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.saldo = saldo

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.correo})"

    def comprar(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            return f"Compra realizada. Saldo restante: ${self.saldo:.2f}"
        return "Saldo insuficiente."

    def recargar_saldo(self, monto):
        self.saldo += monto
        return f"Saldo actualizado: ${self.saldo:.2f}"
