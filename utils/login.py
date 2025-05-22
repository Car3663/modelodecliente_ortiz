def login(correo, lista_clientes):
    for cliente in lista_clientes:
        if cliente.correo == correo:
            return cliente
    return None
