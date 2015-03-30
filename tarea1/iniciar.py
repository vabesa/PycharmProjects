__author__ = 'Vicente Besa'
from especificaciones import *
pasajeros={}
viajes={}
cargas={}
itinerarios={}
modelos_vehiculos={}
flota={}
ciudades={}
rutas={}
terminales={}
dciudades={}
class Iniciar():
    def __init__(self):
        Generar.generar_rutas()
        Generar.generar_ciudades()
        Generar.generar_pasajeros()
        Generar.generar_cargas()
        Generar.generar_vehiculos()
        Generar.generar_viajes()
        Generar.generar_itinerarios()
class Generar():
    def generar_rutas():
            datos_rutas=open("routes.txt", "r")
            i=0
            global rutas
            for linea in datos_rutas:
                if i==0:
                    i=1
                    continue
                lista=linea.strip('\n').split('\t')
                rutas[lista[0]]=Ruta(lista[1],lista[2],lista[0],lista[3],lista[4],lista[5],lista[6])
            datos_rutas.close()
    def generar_ciudades():
        #generar diccionario de ciudades
        datos_ciudad=open("cities.txt", "r")
        global ciudades
        j=0
        i=0
        for linea in datos_ciudad:
            if i==0:
                i=1
                continue
            lista=linea.strip("\n").split("\t")
            ciudades[lista[0]]=Ciudad(lista[0],lista[1])
            dciudades[lista[0]]=j
            j+=1
        datos_ciudad.close()
        ## generar terminales
        datos_terminales=open("hubs.txt", "r")
        i=0
        for linea in datos_terminales:
            if i==0:
                i=1
                continue
            linea.strip("\n")
            linea2=linea.split()
            var_aux1="Airports".split()
            var_aux2="BusTerminals".split()
            var_aux3="CargoDepots".split()
            var_aux4="Harbors".split()
            if linea2==var_aux1 or linea2==var_aux2 or linea2==var_aux3 or linea2==var_aux4:
                continue

            lista=linea.strip("\n").split("\t")
            terminales[lista[0]]=Terminal(lista[0],lista[2],lista[3],lista[1])
            ciudades[lista[1]].agregar_terminal(terminales[lista[0]])
        datos_terminales.close()
    def generar_pasajeros():
        # generar diccionario de pasajeros#
        datos = open("passengers.txt", "r")
        global pasajeros
        i=0
        for linea in datos:
            if i == 0:
                i = 1
                continue
            lista=linea.strip('\n').split('\t')
            pasajeros[lista[2]]=Pasajero(lista[0],lista[1],lista[2])
        datos.close()
    def generar_cargas():
        # Generar cargas
        datos_carga=open("cargo.txt", "r")
        global cargas
        i=0
        for linea in datos_carga:
            if i==0:
                i=1
                continue
            lista=linea.strip('\n').split('\t')
            cargas[lista[0]]=Carga(lista[0],lista[1],lista[2],lista[3],lista[4])
        datos_carga.close()
    def generar_viajes():    # generar viajes
        datos_viajes=open("trips.txt", "r")
        global viajes
        i=0
        for linea in datos_viajes:
            if i==0:
                i=1
                continue
            lista=linea.strip('\n').split('\t')
            viajes[lista[0]]=Viaje(lista[0],lista[1],lista[2],lista[4],lista[5],lista[3],rutas[lista[3]].largo,flota[lista[5]].velocidad,float(rutas[lista[3]].multiplicador_costo)*float(flota[lista[5]].costo_transporte)*float(rutas[lista[3]].largo))
            flota[lista[5]].agregar_viaje(viajes[lista[0]])
        datos_viajes.close()
    def generar_vehiculos():
        # generar vehiculo
        datos_modelos = open("vehicle_models.txt","r")
        i=0
        for linea in datos_modelos:
            linea.strip('\n')
            linea2=linea.split()
            var_aux1="Airplane".split()
            var_aux2="CargoShip".split()
            var_aux3="CruiseShip".split()
            var_aux4="Bus".split()
            var_aux5="Truck".split()
            if linea2==var_aux1:
                last_one=1
                i=0
                continue
            elif linea2==var_aux2:
                last_one=2
                i=0
                continue
            elif linea2==var_aux3:
                last_one=3
                i=0
                continue
            elif linea2==var_aux4:
                last_one=4
                i=0
                continue
            elif linea2==var_aux5:
                last_one=5
                i=0
                continue
            if last_one==1:
                if i==0:
                    i=1
                    continue
                lista=linea.strip('\n').split('\t')
                lista.append("avion")
                modelos_vehiculos[lista[0]]=lista
            if last_one==2:
                if i==0:
                    i=1
                    continue
                lista=linea.strip('\n').split('\t')
                lista.append("barco")
                modelos_vehiculos[lista[0]]=lista
            if last_one==3:
                if i==0:
                    i=1
                    continue
                lista=linea.strip('\n').split('\t')
                lista.append("crucero")
                modelos_vehiculos[lista[0]]=lista
            if last_one==4:
                if i==0:
                    i=1
                    continue
                lista=linea.strip('\n').split('\t')
                lista.append("bus")
                modelos_vehiculos[lista[0]]=lista
            if last_one==5:
                if i==0:
                    i=1
                    continue
                lista=linea.strip('\n').split('\t')
                lista.append("camion")
                modelos_vehiculos[lista[0]]=lista
        datos_modelos.close()
        datos_flota=open('fleet.txt','r')
        global flota
        i=0
        for linea in datos_flota:
            if i==0:
                i=1
                continue
            lista=linea.strip('\n').split('\t')
            elemento=modelos_vehiculos[lista[0]]
            if elemento[-1]=="avion":
                vehiculo_aux=Avion(elemento[4],"Aereo",elemento[5],elemento[6],elemento[7],lista[1],"Avion",elemento[1],elemento[2],elemento[8])
                flota[lista[1]]=vehiculo_aux
                continue
            elif elemento[-1]=="barco":
                vehiculo_aux=Barco(elemento[3],elemento[4],elemento[5],"Acuatico",lista[1],"Barco",elemento[1],elemento[2],elemento[6])
                flota[lista[1]]=vehiculo_aux
                continue
            elif elemento[-1]=="crucero":
                vehiculo_aux=Crucero(elemento[3],"Acuatico",lista[1],"Crucero",elemento[1],elemento[2],elemento[4])
                flota[lista[1]]=vehiculo_aux
                continue
            elif elemento[-1]=="bus":
                vehiculo_aux=Bus(elemento[3],"Terrestre",lista[1],"Bus",elemento[1],elemento[2],elemento[4])
                flota[lista[1]]=vehiculo_aux
                continue
            elif elemento[-1]=="camion":
                vehiculo_aux=Camion(elemento[3],elemento[4],elemento[5],"Terrestre",lista[1],"Camión",elemento[1],elemento[2],elemento[6])
                flota[lista[1]]=vehiculo_aux
                continue
        datos_flota.close()

    def generar_itinerarios():        # generar itinerarios
        datos_itinerarios= open("itineraries.txt", "r")
        global itinerarios
        i=0
        for linea in datos_itinerarios:
            if i==0:
                i=1
                continue
            lista=linea.strip('\n').split('\t')
            id_viajes=lista[1].split(' ')
            viajes_aux=[]
            for id in id_viajes:
                try:
                    pasajeros[lista[0]].agregar_viaje(viajes[id])
                    viajes[id].agregar_contenido(pasajeros[lista[0]])
                except:
                    1
                try:
                    cargas[lista[0]].agregar_viaje(viajes[id])
                    viajes[id].agregar_contenido(cargas[lista[0]])
                except:
                    1

        datos_itinerarios.close()
