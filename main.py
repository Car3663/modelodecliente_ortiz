from cliente.cliente import Cliente
from cliente.premium import ClientePremium
from utils.login import login


clientes = [
    Cliente("Ana", "Pérez", "ana@mail.com", 1500),
    ClientePremium("Luis", "Gómez", "luis@mail.com", 3000, descuento=10)
]


correo = input("Ingrese su correo para iniciar sesión: ")
cliente_activo = login(correo, clientes)

if cliente_activo:
    print(f"Bienvenido/a {cliente_activo}")
    print(f"Tipo de cliente: {cliente_activo.tipo}")
    opcion = input("¿Desea realizar una compra (c) o recargar saldo (r)? ")

    if opcion == "c":
        monto = float(input("Ingrese el monto de la compra: "))
        print(cliente_activo.comprar(monto))
    elif opcion == "r":
        monto = float(input("Ingrese el monto a recargar: "))
        print(cliente_activo.recargar_saldo(monto))
else:
    print("Correo no encontrado.")
