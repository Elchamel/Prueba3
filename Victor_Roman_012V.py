# Evaluacion numero 3
import csv
print("Bienvenido a Catpremiun")

def registro_pedido(pedido):
nombre = input("Ingrese nombre y apellido:")
direccion = print("Ingreser Direccion: ")
sector = print("Ingrese uno de estos sectores: San Bernardo,Calera de Tango,Buin: ")

while True:
    saco = input("Ingrese el saco que desea comprar (5kg,10kg,20kg): ")
    if saco == "5kg":
        saco5kg = input(int("Ingrese la cantidad de sacos que desea: "))
        saco5kg = saco5kg

    elif saco == "10kg":
        saco10kg = input(int("Ingrese la cantidad de sacos que desea: "))
        saco10kg = saco10kg

    elif saco == "20kg":
        saco20kg = input(int("Ingrese la cantidad de sacos que desea: "))
        saco20kg = saco20kg

    else:
        print("Ingrese una opcion valida")

    pedido = {"Nombre",nombre,
              "Direccion",direccion,
              "Sector",sector,
              "Sacos5kg",saco5kg,
              "Sacos10kg",saco10kg,
              "sacos20kg",saco20kg}
    
    def imprimir_hoja_ruta(pedidos):
        opcion_pedido = input("Desea Imprimir el pedido segun sector: ")
        if opcion_pedido == "sector":
            sector_ = input("Ingresa sector: San bernardo,Calera de tango,Buin: ")
            pedido_imprimir = [pedido for trabajador in pedidos if pedido['sector'] == sector]
        else:
            pedido_imprimir = pedidos

        with open (f"planilla_{opcion_pedido}.txt", "w") as archivo:
            archivo.write(f"nombre":[nombre] "direccion",[direccion],"sector",[sector])
            print(f"hoja guardada en 'planilla_{opcion_pedido}.txt'\n")

        with open ("archivo.csv","a",newline="")as archivo:
            archivo.write(f"nombre":[nombre] "direccion",[direccion],"sector",[sector])
            

    
    pedidos = []
   
    
    while True:
        print("1. Registrar pedido")
        print("2. listar todos los pedidos")
        print("3. Imprimir hoja de ruta")
        print("4. Salir del programa")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registro_pedido(pedido)
        elif opcion == "2":
            listar_pedidos(pedido)
        elif opcion == "3":
            imprimir_hoja_ruta(pedido)
        elif opcion == "4":
            print("Saliendo del programa.")
        break
    else:
        print("Opción no válida, intente de nuevo.\n")
        

   