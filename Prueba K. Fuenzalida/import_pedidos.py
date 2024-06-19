datos_del_pedido = []

def registrar_pedido(datos_del_pedido):
    while True:
        nombre = input("Ingrese su nombre y apellido: ")
        if nombre != "":
            datos_del_pedido = nombre
            break
        else:
            print("Ingrese un nombre valido")
    
    while True:
        direccion = input("Ingrese su direccion: ")
        if direccion != "":
            datos_del_pedido = direccion
            break
        else:
            print("Ingrese una direccion valida")

    while True:
        sector = input("Ingrese su sector: ")
        if sector != "":
            datos_del_pedido = sector
            break
        else:
            print("Ingrese un sector valido")

    while True:
        detalles_pedido = input("Ingrese un tipo de paquete\n(pequeño/mediano/grande)\n--> ").upper()
        if detalles_pedido == "PEQUEÑO":
            datos_del_pedido = detalles_pedido
            break
        elif detalles_pedido == "MEDIANO":
            datos_del_pedido = detalles_pedido
            break
        elif detalles_pedido == "GRANDE":
            datos_del_pedido = detalles_pedido
            break
        else:
            print("Detalle invalido\nDebe escribir: pequeño o mediano o grande)\n")

    while True:
        try:
            cantidad = int(input("Eliga la cantidad del pedido: "))
            datos_del_pedido = cantidad
            break
        except ValueError:
            print("Ingrese una opcion valida")
            
    datos_del_pedido = {
        "Cliente" : nombre,
        "Direccion" : direccion,
        "Sector" : sector,
        "Paquetes" : detalles_pedido,
        "Cantidad" : cantidad
    }

def listar_pedidos(datos_del_pedido):
    print(datos_del_pedido)
    
def imprimir_hoja_ruta(datos_del_pedido):
    sector = input("Ingrese el sector (Centro/Norte/Sur)\n--> ").upper()
    if sector == "CENTRO" or sector == "NORTE" or sector == "SUR":
        with open("archivo.txt","w") as archivo:
            archivo.write(datos_del_pedido)