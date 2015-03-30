class Pasajero():
    def __init__(self, nombre, apellido, RUT):
        self.nombre=nombre
        self.apellido=apellido
        self.RUT=RUT
        self.viajes=[]
    def imprimir(self):
        print("nombre: {},apellido: {}, RUT: {}".format(self.nombre,self.apellido,self.RUT))
        print("-----------------------------------------------------------------------------------------------------")
    def agregar_viaje(self,viaje):
        self.viajes.append(viaje)
    def obtener_ubicacion(self,fecha,hora):
        lista=fecha.split('/')
        lista2=hora.split(':')
        dia=int(lista[0])+int(lista[1])*30+int(lista[2])*30*12
        hora_min=int(lista2[0])*60+int(lista2[1])
        minutos_ingresados=dia*24*60+hora_min
        k=0
        primera=True
        ultimos_minutos=0
        for i in range(len(self.viajes)):
            fecha_hora=self.viajes[i].hora_partida
            fecha_hora=fecha_hora.split("-")
            fecha=fecha_hora[0].split('/')
            hora=fecha_hora[1].split(':')
            minutos_vuelo=(int(fecha[0])+int(fecha[1])*30+int(fecha[2])*30*12)*24*60+int(hora[0])*60+int(hora[1])
            if minutos_ingresados>=minutos_vuelo and minutos_ingresados<=minutos_vuelo+60*self.viajes[i].tiempo:
                k=i
                return [k,"ENTRE"]
            if minutos_ingresados>=minutos_vuelo and minutos_vuelo>ultimos_minutos:
                ultimos_minutos=minutos_vuelo
                k=i
                primera=False
        return [k,primera]
    def obtener_distancia(self,fecha,hora):
        lista=fecha.split('/')
        lista2=hora.split(':')
        dia=int(lista[0])+int(lista[1])*30+int(lista[2])*30*12
        hora_min=int(lista2[0])*60+int(lista2[1])
        minutos_ingresados=dia*24*60+hora_min
        distancia=0
        for i in range(len(self.viajes)):
            fecha_hora=self.viajes[i].hora_partida
            fecha_hora=fecha_hora.split("-")
            fecha=fecha_hora[0].split('/')
            hora=fecha_hora[1].split(':')
            minutos_vuelo=(int(fecha[0])+int(fecha[1])*30+int(fecha[2])*30*12)*24*60+int(hora[0])*60+int(hora[1])
            if minutos_ingresados>=minutos_vuelo and minutos_ingresados<=minutos_vuelo+self.viajes[i].tiempo:
                distancia+=(minutos_vuelo+self.viajes[i].tiempo-minutos_ingresados)*self.viajes[i].velocidad/60
            elif minutos_ingresados>=minutos_vuelo:
                distancia+=self.viajes[i].largo
        print("El pasajero de RUT {} ha recorrido {} km".format(self.RUT,distancia))
    def imprimir_itinerario(self):
        print("Los viaje para el pasajero de RUT: {} son".format(self.RUT))
        for viaje in self.viajes:
            viaje.imprimir()
            print("Costo: {}".format(viaje.costo_base))
            print("-----------------------------------------------------------------------------------------------")


class Itinerario():
    def __init__(self,rut,viajes):
        self.rut=rut
        self.viajes=viajes
    def imprimir(self):
        for viaje in self.viajes:
            viaje.imprimir()


class Carga():
    def __init__(self,id,nombre, peso, volumen, tipo):
        self.id=id
        self.nombre=nombre
        self.peso=peso
        self.volumen=volumen
        self.tipo=tipo
        self.viajes=[]
    def imprimir(self):
        print("Nombre: {}, Peso: {}, Volumen: {}, Tipo: {}".format(self.nombre,self.peso,self.volumen,self.tipo))
        print("-----------------------------------------------------------------------------------------------------")
    def agregar_viaje(self,viaje):
        self.viajes.append(viaje)
    def obtener_ubicacion(self,fecha,hora):
        lista=fecha.split('/')
        lista2=hora.split(':')
        dia=int(lista[0])+int(lista[1])*30+int(lista[2])*30*12
        hora_min=int(lista2[0])*60+int(lista2[1])
        minutos_ingresados=dia*24*60+hora_min
        k=0
        primera=True
        ultimos_minutos=0
        for i in range(len(self.viajes)):
            fecha_hora=self.viajes[i].hora_partida
            fecha_hora=fecha_hora.split("-")
            fecha=fecha_hora[0].split('/')
            hora=fecha_hora[1].split(':')
            print(hora)
            minutos_vuelo=(int(fecha[0])+int(fecha[1])*30+int(fecha[2])*30*12)*24*60+int(hora[0])*60+int(hora[1])
            if minutos_ingresados>=minutos_vuelo and minutos_ingresados<=minutos_vuelo+self.viajes[i].tiempo*60:
                return [k,"ENTRE"]
            if minutos_ingresados>=minutos_vuelo and minutos_vuelo>ultimos_minutos:
                ultimos_minutos=minutos_vuelo
                k=i
                primera=False
        return [k,primera]
    def imprimir_itinerario(self):
        print("Los viajes para la carga de id {} son".format(self.id))
        for viaje in self.viajes:
            viaje.imprimir()
        print("Costo: {}".format(viaje.costo_base*max(float(self.peso)/100,float(self.volumen))))


class Terminal():
    def __init__(self,nombre,tipo_transporte,capacidad_maxima,ciudad):
        self.nombre=nombre
        self.tipo_transporte=tipo_transporte
        self.capacidad_maxima=capacidad_maxima
        self.ciudad=ciudad
    def imprimir(self):
        print("Nombre: {}, Tipo de transporte: {}, Capacidad maxima: {}".format(self.nombre, self.tipo_transporte, self.capacidad_maxima))


class Ruta():
    def __init__(self,ciudad1,ciudad2,nombre,tipo_vehiculos,largo,tamaño,multiplicador_costo):
        self.ciudad1=ciudad1
        self.ciudad2=ciudad2
        self.nombre=nombre
        self.tipo_vehiculos=tipo_vehiculos
        self.largo=largo
        self.tamaño=tamaño
        self.multiplicador_costo=multiplicador_costo
    def imprimir(self):
        print("Ciudades: {} y {}, nombre: {}, tipo de vehiculos que soporta: {}, largo de la ruta: {}, multiplicador de costo: {}".format(self.ciudad1,self.ciudad2,self.nombre,self.tipo_vehiculos,self.largo,self.multiplicador_costo))


class TransporteCarga():
    def __init__(self,volumen_maximo,peso_maximo,tipo_carga,medio_viaje="None"):
        self.volumen_maximo=volumen_maximo
        self.peso_maximo=peso_maximo
        self.tipo=tipo_carga
        self.medio_viaje=medio_viaje
    def imprimir(self):
        print("volumen maximo: {},peso maximo: {},tipo de carga: {}, medio en que viaja: {}".format(self.volumen_maximo,self.peso_maximo,self.tipo,self.medio_viaje))


class TransportePasajeros():
    def __init__(self,cantidad_asientos,medio_viaje):
        self.cantidad_asientos=cantidad_asientos
        self.medio_viaje=medio_viaje
    def imprimir(self):
        print("Cantidad de asientos: {}, Medio en que viaja: {}".format(self.cantidad_asientos,self.medio_viaje))


class Vehiculo():

    def __init__(self,nombre,tipo,tamaño,velocidad,costo_transporte):
        self.nombre=nombre
        self.tipo=tipo
        self.tamaño=tamaño
        self.velocidad=velocidad
        self.costo_transporte=costo_transporte
        self.viajes=[]
    def imprimir(self):
        print("Nombre: {}, Tipo de vehiculo: {}, Tamaño: {}, Velocidad: {}, Costo de transporte: {}".format(self.nombre,self.tipo,self.tamaño,self.velocidad,self.costo_transporte))
    def agregar_viaje(self,viaje):
        self.viajes.append(viaje)
    def obtener_ubicacion(self,fecha,hora):
        lista=fecha.split('/')
        lista2=hora.split(':')
        dia=int(lista[0])+int(lista[1])*30+int(lista[2])*30*12
        hora_min=int(lista2[0])*60+int(lista2[1])
        minutos_ingresados=dia*24*60+hora_min
        k=0
        ultimos_minutos=0
        primera=True
        for i in range(len(self.viajes)):
            fecha_hora=self.viajes[i].hora_partida
            fecha_hora=fecha_hora.split("-")
            fecha=fecha_hora[0].split('/')
            hora=fecha_hora[1].split(':')
            minutos_vuelo=(int(fecha[0])+int(fecha[1])*30+int(fecha[2])*30*12)*24*60+int(hora[0])*60+int(hora[1])
            if minutos_ingresados>=minutos_vuelo and minutos_ingresados<=minutos_vuelo+self.viajes[i].tiempo:
                return [k,"ENTRE"]
            if minutos_ingresados>=minutos_vuelo and minutos_vuelo>ultimos_minutos:
                ultimos_minutos=minutos_vuelo
                k=i
                primera=False
        return [k,primera]
    def obtener_distancia(self,fecha,hora):
        lista=fecha.split('/')
        lista2=hora.split(':')
        dia=int(lista[0])+int(lista[1])*30+int(lista[2])*30*12
        hora_min=int(lista2[0])*60+int(lista2[1])
        minutos_ingresados=dia*24*60+hora_min
        distancia=0
        for i in range(len(self.viajes)):
            fecha_hora=self.viajes[i].hora_partida
            fecha_hora=fecha_hora.split("-")
            fecha=fecha_hora[0].split('/')
            hora=fecha_hora[1].split(':')
            minutos_vuelo=(int(fecha[0])+int(fecha[1])*30+int(fecha[2])*30*12)*24*60+int(hora[0])*60+int(hora[1])
            if minutos_ingresados>=minutos_vuelo and minutos_ingresados<=minutos_vuelo+self.viajes[i].tiempo:
                distancia+=(minutos_vuelo+self.viajes[i].tiempo-minutos_ingresados)*self.viajes[i].velocidad/60
            elif minutos_ingresados>=minutos_vuelo:
                distancia+=self.viajes[i].largo
        print("El vehiculo de nombre {} ha recorrido {} km".format(self.nombre,distancia))


class Avion(TransporteCarga,TransportePasajeros,Vehiculo):
    def __init__(self,cantidad_asientos,medio_viaje,volumen_maximo,peso_maximo,tipo_carga,nombre,tipo,tamaño,velocidad,costo_transporte):
        TransporteCarga.__init__(self,volumen_maximo,peso_maximo,tipo_carga)
        TransportePasajeros.__init__(self,cantidad_asientos,"Aereo")
        Vehiculo.__init__(self,nombre,tipo,tamaño,velocidad,costo_transporte)
    def imprimir(self):
        Vehiculo.imprimir(self)
        TransporteCarga.imprimir(self)
        TransportePasajeros.imprimir(self)
        print("-----------------------------------------------------------------------------------------------------")


class Bus(Vehiculo,TransportePasajeros):
    def __init__(self,cantidad_asientos,medio_viaje,nombre,tipo,tamaño,velocidad,costo_transporte):
        TransportePasajeros.__init__(self,cantidad_asientos,"Terrestre")
        Vehiculo.__init__(self,nombre,tipo,tamaño,velocidad,costo_transporte)
    def imprimir(self):
        Vehiculo.imprimir(self)
        TransportePasajeros.imprimir(self)
        print("-----------------------------------------------------------------------------------------------------")


class Camion(TransporteCarga,Vehiculo):
    def __init__(self,volumen_maximo,peso_maximo,tipo_carga,medio_viaje,nombre,tipo,tamaño,velocidad,costo_transporte):
        TransporteCarga.__init__(self,volumen_maximo,peso_maximo,tipo_carga,"Terrestre")
        Vehiculo.__init__(self,nombre,tipo,tamaño,velocidad,costo_transporte)
    def imprimir(self):
        Vehiculo.imprimir(self)
        TransporteCarga.imprimir(self)
        print("-----------------------------------------------------------------------------------------------------")


class Barco(TransporteCarga,Vehiculo):
    def __init__(self,volumen_maximo,peso_maximo,tipo_carga,medio_viaje,nombre,tipo,tamaño,velocidad,costo_transporte):
        TransporteCarga.__init__(self,volumen_maximo,peso_maximo,tipo_carga,"Acuatico")
        Vehiculo.__init__(self,nombre,tipo,tamaño,velocidad,costo_transporte)
    def imprimir(self):
        Vehiculo.imprimir(self)
        TransporteCarga.imprimir(self)
        print("-----------------------------------------------------------------------------------------------------")


class Crucero(TransportePasajeros,Vehiculo):
    def __init__(self,cantidad_asientos,medio_viaje,nombre,tipo,tamaño,velocidad,costo_transporte):
        TransportePasajeros.__init__(self,cantidad_asientos,"Acuatico")
        Vehiculo.__init__(self,nombre,tipo,tamaño,velocidad,costo_transporte)
    def imprimir(self):
        Vehiculo.imprimir(self)
        TransportePasajeros.imprimir(self)
        print("-----------------------------------------------------------------------------------------------------")


class Viaje():
    def __init__(self,codigo_viaje,terminal_partida,terminal_llegada,hora_partida,vehiculo_utilizado,ruta_utilizada,largo,velocidad,costo_base):
        self.codigo_viaje=codigo_viaje
        self.terminal_partida=terminal_partida
        self.terminal_llegada=terminal_llegada
        self.hora_partida=hora_partida
        self.vehiculo_utilizado=vehiculo_utilizado
        self.ruta_utilizada=ruta_utilizada
        self.tiempo=int(largo)/int(velocidad)
        self.largo=int(largo)
        self.velocidad=int(velocidad)
        self.contenido=[]
        self.costo_base=costo_base
    def imprimir(self):
        print("Codigo de viaje: {}, Terminal de partida: {}, Terminal de llegada: {}, Hora de partida: {}, Vehiculo utilizado: {}, Ruta utilizada: {}".format(self.codigo_viaje,self.terminal_partida,self.termina_llegada,self.hora_partida,self.vehiculo_utilizado,self.ruta_utilizada))
        print("-----------------------------------------------------------------------------------------------------")
    def agregar_contenido(self,contenido):
        self.contenido.append(contenido)


class Ciudad():
    def __init__(self,nombre,pais):
        self.nombre=nombre
        self.pais=pais
        self.terminales=[]
    def agregar_terminal(self,terminal):
        self.terminales.append(terminal)
    def imprimir(self):
        print("Ciudad: {}, Pais: {}".format(self.nombre,self.pais))
        for terminal in self.terminales:
            terminal.imprimir()
