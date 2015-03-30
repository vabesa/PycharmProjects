__author__ = 'Vicente Besa'
import sys
from especificaciones import *
from iniciar import *
Iniciar()
class MenuPrincipal:
    def __init__(self):
        self.opciones = {
                        "1": self.obtener_datos,
                        "2": self.hacer_calculos,
                        "3": self.crear_datos,
                        "4": self.agendar_itinerarios,
                        "5": self.cancelar_pasaje,
                        "6": self.salir
                        }

    def display_menu(self):
        print("""
        Menu:
            1: Obtener datos
            2: Hacer calculos
            3: Crear nuevos objetos
            4: Agendar nuevos itinerarios
            5: Cancelar pasajes agegandos a un objeto
            6: Salir
        """)

    def run(self):

        while True:
            self.display_menu()
            eleccion = input("Ingrese Opcion: ")
            accion = self.opciones.get(eleccion)
            if accion:
                accion()#aqui se llama a la funcion
            else:
                print("{0} no es una opcion valida".format(eleccion))


    def obtener_datos(self):
        MenuConsultas().run()

    def hacer_calculos(self):
        MenuCalculos().run()



    def crear_datos(self):
        MenuCrear().run()

    def agendar_itinerarios(self):
        mensaje = input("Ingrese Mensaje: ")
        tag_list = input("Ingrese Tags separados por espacios: ")
        tag_list = tag_list.split()#separa los strings por espacio y los pone en una lista
        self.panel.nuevo_postit(mensaje, tag_list)
        print("Nota creada exitosamente!!")

    def cancelar_pasaje(self):
        id = input("ingrese el id del Post-It que quiere modificar: ")
        id = int(id)
        mensaje = input("Ingrese el nuevo mensaje: ")
        tag_list = input("Ingrese los nuevos tags separados por espacios: ")
        if mensaje:
            print(id)
            self.panel.modifica_mensaje(id, mensaje)
        if tag_list:
            tag_list = tag_list.split()
            self.panel.modifica_tags(id, tag_list)
        print("postit modificado exitosamente!!")

    def salir(self):
        print("Gracias por usar Transportes Petrov")
        sys.exit(0)
class MenuConsultas():
    def __init__(self):
        self.seguir=True
        self.opciones = {
                        "1": self.imprimir_atributos,
                        "2": self.posicion_objeto,
                        "3": self.informacion_ciudades,
                        "4": self.salir
                        }

    def display_menu(self):
        print(("""
        Menu:
            1: Imprimir atributos de un objeto
            2: Saber posicion de un objeto
            3: Informacion de rutas entre 2 ciudades
            4: volver al menu principal
        """))

    def run(self):

        while self.seguir:
            self.display_menu()
            eleccion = input("Ingrese Opcion: ")
            accion = self.opciones.get(eleccion)
            if accion:
                accion()#aqui se llama a la funcion
            else:
                print("{0} no es una opcion valida".format(eleccion))


    def imprimir_atributos(self):
        id=input("Ingrese el id del objeto que desea saber sus atributos")
        pas=False
        car=False
        via=False
        flo=False
        rut=False
        try:
            pasajeros[id].imprimir()
        except:
            pas=True
        try:
            cargas[id].imprimir()
        except:
            car=True
        try:
            viajes[id].imprimir()
        except:
            via=True
        try:
            flota[id].imprimir()
        except:
            flo=True
        try:
            rutas[id].imprimir()
        except:
            rut=True
        if pas and car and via and flo and rut:
            print("Error al ingresar el id")

    def posicion_objeto(self):
        fecha=input("Ingrese fecha")
        hora=input("Ingrese hora")
        id=input("Ingrese id del objeto")
        car=False
        pas=False
        flo=False
        try:
            lista=cargas[id].obtener_ubicacion(fecha,hora)
            boolean=lista[1]
            k=lista[0]
            if boolean=="ENTRE":
                terminal_partida=cargas[id].viajes[k].terminal_partida
                terminal_llegada=cargas[id].viajes[k].terminal_llegada
                print("La carga de id {}, esta viajando desde {} hasta {}".format(cargas[id].id,terminales[terminal_partida].ciudad,terminales[terminal_llegada].ciudad))
            elif boolean:
                terminal=cargas[id].viajes[k].terminal_partida
            else:
                terminal=cargas[id].viajes[k].terminal_llegada
                print("La carga de id {} esta la ciudad  {}".format(cargas[id].id,terminales[terminal].ciudad))
        except:
            car=True

        try:
            lista=pasajeros[id].obtener_ubicacion(fecha,hora)
            boolean=lista[1]
            k=lista[0]
            if boolean=="ENTRE":
                terminal_partida=pasajeros[id].viajes[k].terminal_partida
                terminal_llegada=pasajeros[id].viajes[k].terminal_llegada
                print("El pasajero de RUT {}, esta viajando desde {} hasta {}".format(pasajeros[id].RUT,terminales[terminal_partida].ciudad,terminales[terminal_llegada].ciudad))
            elif boolean:
                terminal=pasajeros[id].viajes[k].terminal_partida
            else:
                terminal=pasajeros[id].viajes[k].terminal_llegada
                print("El pasajero de RUT {} esta la ciudad {}".format(pasajeros[id].id,terminales[terminal].ciudad))
        except:
            pas=True

        try:
            lista=flota[id].obtener_ubicacion(fecha,hora)
            boolean=lista[1]
            k=lista[0]
            if boolean=="ENTRE":
                terminal_partida=flota[id].viajes[k].terminal_partida
                terminal_llegada=flota[id].viajes[k].terminal_llegada
                print("El vehiculo de nombre {}, esta viajando desde {} hasta {}".format(flota[id].RUT,terminales[terminal_partida].ciudad,terminales[terminal_llegada].ciudad))
            elif boolean:
                terminal=flota[id].viajes[k].terminal_partida
            else:
                terminal=flota[id].viajes[k].terminal_llegada
                print("El pasajero de RUT {} esta la ciudad {}".format(flota[id].id,terminales[terminal].ciudad))
        except:
            flo=True
        if car and pas and flo:
            print("Error al ingresar un dato")

    def informacion_ciudades(self):
        mensaje = input("Ingrese Mensaje: ")
        tag_list = input("Ingrese Tags separados por espacios: ")
        tag_list = tag_list.split()#separa los strings por espacio y los pone en una lista
        self.panel.nuevo_postit(mensaje, tag_list)
        print("Nota creada exitosamente!!")


    def salir(self):
        self.seguir=False
class MenuCalculos():
    def __init__(self):
        self.seguir=True
        self.opciones = {
                        "1": self.calcular_distancia,
                        "2": self.imprimir_itinerarios,
                        "3": self.salir
                        }

    def display_menu(self):
        print(("""
        Menu:
            1: Calcular distancia recorrida por un objeto
            2: Imprimir itinerario de un objeto
            3: volver al menu principal
        """))

    def run(self):

        while self.seguir:
            self.display_menu()
            eleccion = input("Ingrese Opcion: ")
            accion = self.opciones.get(eleccion)
            if accion:
                accion()#aqui se llama a la funcion
            else:
                print("{0} no es una opcion valida".format(eleccion))



    def calcular_distancia(self):
        fecha=input("Ingrese fecha")
        hora=input("Ingrese hora")
        id=input("Ingrese id del objeto")
        car=False
        pas=False
        flo=False
        try:
            cargas[id].obtener_distancia(fecha,hora)
        except:
            car=True
        try:
            pasajeros[id].obtener_distancia(fecha,hora)
        except:
            pas=True
        try:
            flota[id].obtener_distancia(fecha,hora)
        except:
            flo=True

        if car and pas and flo:
            print("Error al ingresar un dato")

    def imprimir_itinerarios(self):
        id=input("Ingrese el identificador del objeto que desea saber su itinerario")
        pas=False
        car=False
        try:
            pasajeros[id].imprimir_itinerario()
        except:
            pas=True
        try:
            cargas[id].imprimir_itinerario()
        except:
            car=True
        if pas and car:
            print("Error al ingresar los datos")



    def salir(self):
        self.seguir=False
class MenuCrear():
    def __init__(self):
        self.seguir=True
        self.opciones = {
                        "1": self.crear_pasajero,
                        "2": self.crear_carga,
                        "3": self.crear_viaje,
                        "4": self.crear_ruta,
                        "5": self.crear_vehiculo,
                        "6": self.salir
                        }

    def display_menu(self):
        print(("""
        Menu:
            1: Crear pasajero
            2: Crear carga
            3: Crear viaje
            4: Crear ruta
            5: Crear vehiculo
            6: Volver al menu principal
        """))

    def run(self):

        while self.seguir:
            self.display_menu()
            eleccion = input("Ingrese Opcion: ")
            accion = self.opciones.get(eleccion)
            if accion:
                accion()#aqui se llama a la funcion
            else:
                print("{0} no es una opcion valida".format(eleccion))



    def crear_pasajero(self):
        print("-------------------------------------------------------------------------------------------------------")
        rut=input("Ingrese RUT del pasajero")
        nombre=input("Ingrese el nombre del pasajero")
        apellido=input("Ingrese el apellido del pasajero")

    def crear_carga(self):
        id=input("Ingrese id de la carga")
        nombre=input("Ingrese el nombre de la carga")
        peso=input("Ingrese el peso de la carga")
        volumen=input("Ingrese el volumen de la carga")
        tipo=input("Ingrese el tipo de carga")


    def crear_viaje(self):
        id=input("Ingrese codigo de viaje")
        origin=input("Ingrese la terminal de origen del viaje")
        destination=input("Ingrese terminal de destino")
        ruta=input("Ingrese ruta que utiliza")
        departure=input("Ingrese fecha y hora separada por guion, ejemplo : 2/04/2015")
        vehicle=input("Ingrese el vehiculo utilizado")

    def crear_ruta(self):
        id=input("Ingrese el codigo de la ruta")
        ciudad1=input("Ingrese la ciudad N°1")
        ciudad2=input("Ingrese la ciudad N°2")
        tipo=input("Ingrese el tipo de vehiculos")
        lenght=input("Ingrese el largo de la ruta")
        size=input("Ingrese el tamaño que soporta la ruta")
        cost=input("Ingrese el costo de la ruta")

    def crear_vehiculo(self):
        modelo=input("Ingrese el modelo del vehiculo")
        nombre=input("Ingrese el nombre del vehiculo")

    def salir(self):
        self.seguir=False
MenuPrincipal().run()