class Pasajero():
    def __init__(self, nombre, apellido, RUT):
        self.nombre=nombre
        self.apellido=apellido
        self.RUT=RUT
        self.itinerarios=[]
    def imprimir(self):
        print("nombre: {},apellido: {}, RUT: {}".format(self.nombre,self.apellido,self.RUT))
        for itinerario in self.itinerarios:
            itinerario.imprimir()
        print("-----------------------------------------------------------------------------------------------------")
    def agregar_itinerario(self,itineario):
        self.itinerarios.append(itineario)


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
        self.itinerarios=[]
    def imprimir(self):
        print("Nombre: {}, Peso: {}, Volumen: {}, Tipo: {}".format(self.nombre,self.peso,self.volumen,self.tipo))
        for itinerario in self.itinerarios:
            itinerario.imprimir()
        print("-----------------------------------------------------------------------------------------------------")
    def agregar_itinerario(self,itinerario):
        self.itinerarios.append(itinerario)


class Terminal():
    def __init__(self,nombre,tipo_transporte,capacidad_maxima,ciudad):
        self.nombre=nombre
        self.tipo_transporte=tipo_transporte
        self.capacidad_maxima=capacidad_maxima
        self.ciudad=ciudad
    def imprimir(self):
        print("Nombre: {}, Tipo de transporte: {}, Capacidad maxima: {}".format(self.nombre, self.tipo_transporte, self.capacidad_maxima))


class Ruta():
    def __init__(self,ciudades,nombre,tipo_vehiculos,largo,multiplicador_costo):
        self.ciudades=ciudades
        self.nombre=nombre
        self.tipo_vehiculos=tipo_vehiculos
        self.largo=largo
        self.multiplicador_costo=multiplicador_costo
    def imprimir(self):
        print("Ciudades: {} y {}, nombre: {}, tipo de vehiculos que soporta: {}, largo de la ruta: {}, multiplicador de costo: {}".format(self.ciudades[0],self.ciudades[1],self.nombre,self.tipo_vehiculos,self.largo,self.multiplicador_costo))


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
    def imprimir(self):
        print("Nombre: {}, Tipo de vehiculo: {}, Tamaño: {}, Velocidad: {}, Costo de transporte: {}".format(self.nombre,self.tipo,self.tamaño,self.velocidad,self.costo_transporte))


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
    def __init__(self,codigo_viaje,terminal_partida,terminal_llegada,hora_partida,vehiculo_utilizado,ruta_utilizada):
        self.codigo_viaje=codigo_viaje
        self.terminal_partida=terminal_partida
        self.termina_llegada=terminal_llegada
        self.hora_partida=hora_partida
        self.vehiculo_utilizado=vehiculo_utilizado
        self.ruta_utilizada=ruta_utilizada
    def imprimir(self):
        print("Codigo de viaje: {}, Terminal de partida: {}, Terminal de llegada: {}, Hora de partida: {}, Vehiculo utilizado: {}, Ruta utilizada: {}".format(self.codigo_viaje,self.terminal_partida,self.termina_llegada,self.hora_partida,self.vehiculo_utilizado,self.ruta_utilizada))
        print("-----------------------------------------------------------------------------------------------------")

class Ciudad():
    def __init__(self,nombre,pais):
        self.nombre=nombre
        self.pais=pais
