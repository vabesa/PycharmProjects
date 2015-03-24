__author__ = 'Vicente Besa'
class Bodega:
    def __init__(self):
        self.lista_objetos=[]
    def agregar_objeto(self,objeto):
        self.lista_objetos.append(objeto)
    def imprimir_objetos(self):
        for objeto in self.lista_objetos:
            objeto.imprimir()
class Objetos:
    def __init__(self,peso,volumen):
        self.peso=peso
        self.volumen=volumen

class Electronicos:
    def __init__(self,voltaje,consumo_energetico):
        self.voltaje=voltaje
        self.consumo_energetico=consumo_energetico
class Vestibles:
    def __init__(self,talla,tipo_material):
        self.talla=talla
        self.tipo_material=tipo_material
class Lujo:
    def __init__(self,costo):
        self.costo=costo
class Ilicitos:
    def __init__(self,mensaje_alerta):
        self.mensaje_alerta=mensaje_alerta
class Domesticos:
    def __init__(self,reseña):
        self.reseña=reseña
class ObrasArte:
    def __init__(self,nombre,autor,año):
        self.nombre=nombre
        self.autor=autor
        self.año=año
class Comestibles:
    def __init__(self,calorias):
        self.calorias=calorias
#Aqui van los objetos que heredan de las demas
class Refrigerador(Electronicos,Domesticos,Objetos):
    def __init__(self,voltaje,consumo_energetico,reseña,peso,volumen):
        Objetos.__init__(self,peso,volumen)
        Electronicos.__init__(self,voltaje,consumo_energetico)
        Domesticos.__init__(self,reseña)
    def imprimir(self):
        print("")
        print("")
        print("El refrigerador tiene las siguientes caracteristicas:")
        print("el voltaje es: "+str(self.voltaje))
        print("El consumo energetico es: "+str(self.consumo_energetico))
        print("Reseña: "+str(self.reseña))
        print("Peso: "+str(self.peso)+", volumen: "+str(self.volumen))
class AppleWatchDorado(Lujo,Electronicos,Vestibles,Objetos):
    def __init__(self,costo,voltaje,consumo_energetico,talla,tipo_material,peso,volumen):
        Lujo.__init__(self,costo)
        Objetos.__init__(self,peso,volumen)
        Electronicos.__init__(self,voltaje,consumo_energetico)
        Vestibles.__init__(self,talla,tipo_material)
    def imprimir(self):
        print("")
        print("")
        print("El Apple Watch dorado tiene las siguientes caracteristicas ")
        print("El costo es : "+str(self.costo))
        print("el voltaje es: "+str(self.voltaje))
        print("El consumo energetico es: "+str(self.consumo_energetico))
        print("El tipo de material es: "+str(self.tipo_material))
        print("Peso: "+str(self.peso)+", volumen: "+str(self.volumen))

class ArteRobado(Ilicitos,ObrasArte,Objetos):
    def __init__(self,mensaje_alerta,nombre,autor,año,peso,volumen):
        Objetos.__init__(self,peso,volumen)
        Ilicitos.__init__(self,mensaje_alerta)
        ObrasArte.__init__(self,nombre,autor,año)
    def imprimir(self):
        print("")
        print("")
        print("La Mona Lisa robada tiene las siguietes caracteristicas: ")
        print(self.mensaje_alerta)
        print("nombre: "+str(self.nombre)+", autor: "+str(self.autor)+", año: "+str(self.año))
        print("La Mona Lisa es invaluable")
        print("Peso: "+str(self.peso)+", volumen: "+str(self.volumen))
class AbrigoIlegal(Ilicitos,Vestibles,Lujo,Objetos):
    def __init__(self,mensaje_alerta,talla,tipo_material,costo,peso,volumen):
        Objetos.__init__(self,peso,volumen)
        Ilicitos.__init__(self,mensaje_alerta)
        Vestibles.__init__(self,talla,tipo_material)
        Lujo.__init__(self,costo)
    def imprimir(self):
        print("")
        print("")
        print("El abrigo de piel de animal tiene los siguientes atributos: ")
        print(self.mensaje_alerta)
        print("talla: "+str(self.talla)+ ", material: "+str(self.mensaje_alerta))
        print("Costo del abrigo: "+str(self.costo))
        print("Peso: "+str(self.peso)+", volumen: "+str(self.volumen))
class JarronTe(Lujo,ObrasArte,Domesticos,Objetos):
    def __init__(self,costo,nombre,autor,año,reseña,peso,volumen):
        Objetos.__init__(self,peso,volumen)
        Lujo.__init__(self,costo)
        ObrasArte.__init__(self,nombre,autor,año)
        Domesticos.__init__(self,reseña)
    def imprimir(self):
        print("")
        print("")
        print("El jarron de te chino del siglo X tiene las siguientes caracteristicas")
        print("Esta evaluado en :"+str(self.costo))
        print("nombre: "+str(self.nombre)+", autor: "+str(self.autor)+", año: "+str(self.año))
        print("Peso: "+str(self.peso)+", volumen: "+str(self.volumen))
class PapasFritas(Comestibles,Objetos):
    def __init__(self,calorias,peso,volumen):
        Comestibles.__init__(self,calorias)
        Objetos.__init__(self,peso,volumen)
    def imprimir(self):
        print("")
        print("")
        print("Los atributos de las papas fritas son: ")
        print("Calorias: "+str(self.calorias))
        print("Peso: "+str(self.peso)+", volumen: "+str(self.volumen))
# AQUI EMPIEZA EL CODIGO DE TRABAJO
bodega=Bodega()
refrigerador=Refrigerador("220 V","1000 W","El refrigerador es un objeto domestico que va en la cocicna","200 KG","2 Metros cubicos")
reloj=AppleWatchDorado("10,000 USD","12 V","30 W","normal","Oro","250 gramos","2 cm cubicos")
monalisa=ArteRobado("Esta obra de arte fue robada del luvre","Mona Lisa(Gioconda)","Leonardo Da Vinci","finalizada en 1517","1 KG","0,1 Metros cubicos")
abrigo=AbrigoIlegal("Este abrigo es de piel de panda, animal que esta en peligro de extincion","Xl","Piel de panda","1 Millon USD","2 KG","0,5 metros cubicos")
jarron=JarronTe("500,000 USD","Jarron ming","Desconocido","siglo X","Este jarron fue muy importante para la dinastia Qing,ya que la gente hacia fila para ir a apreciarlo","500 gramos","0,2 metros cubicos")
papas=PapasFritas("500 KCalorias","60 gramos","20 cm cubicos")
bodega.agregar_objeto(refrigerador)
bodega.agregar_objeto(reloj)
bodega.agregar_objeto(monalisa)
bodega.agregar_objeto(abrigo)
bodega.agregar_objeto(jarron)
bodega.agregar_objeto(papas)
bodega.imprimir_objetos()