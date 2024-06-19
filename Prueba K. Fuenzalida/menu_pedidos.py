# Desarrolle una aplicación en Python utilizando Visual Studio que permita resolver el siguiente caso:
# La empresa de reparto de paquetes a domicilio "PaquExpress" necesita desarrollar un sistema que permita registrar los pedidos antes de enviar su camión repartidor. Para el funcionamiento del sistema se requieren las siguientes funcionalidades
# 1. Registrar pedido
# 2. Listar los todos los pedidos
# 3. Imprimir hoja de ruta
# 4. Salir del programa
# 1. Registrar pedido
# - Solicitar los siguientes datos del cliente:
# - Nombre y apellido
# - Dirección
# - Sector
# - Detalle del pedido
# - El detalle del pedido debe permitir seleccionar entre 3 tipos de paquetes (pequeño, mediano y grande) y la cantidad de cada uno.
# - Validar que todos los datos sean ingresados correctamente.
# - Ejemplo de registro de pedido:
# ```
# Cliente: Juan Pérez
# Dirección: Calle del Sol 456
# Sector: Centro
# Paquetes: Pequeño - 2, Mediano - 1, Grande - 0
# ```
# Debe validar que todos los datos sean ingresados.
# 2. Listar Pedidos
# Debe mostrar en la pantalla la lista de todos los pedidos realizados similar al ejemplo anterior de registro de pedidos.
# 3. Imprimir hoja de ruta
# - Permitir al usuario seleccionar uno de los sectores predefinidos (Centro, Norte, Sur).
# - Generar un archivo de texto (.txt) con el detalle de los pedidos para el sector seleccionado.
# - El archivo de texto debe seguir el formato del registro completo de pedidos.
# Cada opción de la aplicación debe desarrollarse en una función que debe llamarse desde el programa principal.
import import_pedidos as ip

datos_del_pedido = []

opcion = None

while opcion != 4:
    print("~~~~~~~~~~~~~~~~~~~~~~")
    print("      PaquExpress     ")
    print("~~~~~~~~~~~~~~~~~~~~~~")
    print("1.- Registrar pedido")
    print("2.- Listar todos los pedidos")
    print("3.- Imprimir hoja de ruta")
    print("4.- Salir del programa")
    try:
        opcion = int(input("--> "))

        if opcion == 1:
            print("")
            ip.registrar_pedido(datos_del_pedido)
            
        elif opcion == 2:
            ip.listar_pedidos(datos_del_pedido)
        
        elif opcion == 3:
            ip.imprimir_hoja_ruta(datos_del_pedido)

        elif opcion == 4:
            print("Saliendo...")
        
        else:
            print("Opcion invalida, eliga opcion del 1 al 4")
    except ValueError:
        print("Opcion invalida, eliga opcion del 1 al 4")