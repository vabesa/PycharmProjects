from especificaciones import *
from iniciar import *
Iniciar()
while True:
    print("""
        Menu:
            1: Obtener datos
            2: Crear nuevos objetos
            3: Agendar nuevos itinerarios
            4: Cancelar pasajes agegandos a un objeto
            5: Salir
        """)
    a=input()
    try:
        pasajeros[a].imprimir()
    except:
        1
    try:
        viajes[a].imprimir()
    except:
        1
    try:
        flota[a].imprimir()
    except:
        1
    try:
        cargas[a].imprimir()
    except:
        1