class libreria:
    def __init__(self):
        self.estantes=[]
    def agregar_estante(self,estante):
        self.estante+=[estante]
    def imprimir_topico(self,id_estante):
        print(self.estantes[id_estante].topico)
    def imprimir_topicos(self):
        for i in len(self.estantes):
            print(self.estantes[i].topico)


class estante:
    def __init__(self,cantidadMaxima,topico):
        global id_estanteria
        self.cantidadMaxima=cantidadMaxima
        self.topico=topico
        self.id=id_estanteria
        self.libros=[]
        self.cantidad_libro=0
        id_estanteria+=1

    def agregar_libro(self,libro):
        if self.cantidad_libro < self.cantidadMaxima:
            self.libros+=[libro]
        else:
            print("No se puede agregar ya que el estante esta completo")
    def contar_libros(self,titulo,autor= None):
        contador=0
        for libro in self.libros:
            if libro.titulo==titulo and libro.autor==autor:
                contador+=1
        print('el libro de titulo '+str(titulo)+' y autor '+str(autor)+'tiene '+str(contador)+' ejemplares en el estante de id '+str(self.id))


class libro:
    def __init__(self,titulo,paginas,topico,autor = None):
        global id_libros
        self.id=id_libros
        self.titulo=titulo
        self.paginas=paginas
        self.topico=topico
        self.autor=autor
# el programa empieza aqui
id_libros=0
id_estanteria=0
biblioteca=libreria()
libro1=libro("aventuras de coke",10000000000,"aventura","Vicente Besa")
libro2=libro("aventuras de petro",150,"aventura","Coke")
libro3=libro("Llllllh",10000000,"aventura","Lh")
libro4=libro("el pasto es verde",1,"aventura")
libro5=libro("el paso es azul",10,"aventura")
libro6=libro("el agua",10,"maravilloso","Lh")
libro7=libro("el agua",10,"maravilloso","Lh")
libro8=libro("el agua",10,"maravilloso","Lh")
libro9=libro("el fuego",15,"maravilloso")
libro10=libro("el fuego",15,"maravilloso")
libro11=libro("A",1500000,"bacan","Le pole")
libro12=libro("A",1500000,"bacan","Le pole")
libro13=libro("A",1500000,"bacan","Le pole")
libro14=libro("A",1500000,"bacan","Le pole")
libro15=libro("A",1500000,"bacan","Le pole")
est1=estante(10,"bacan")
est2=estante(15,"aventura")
est3=estante(8,"maravilloso")
est1.agregar_libro(libro11)
est1.agregar_libro(libro12)
est1.agregar_libro(libro13)
est1.agregar_libro(libro14)
est1.agregar_libro(libro15)
est2.agregar_libro(libro1)
est2.agregar_libro(libro2)
est2.agregar_libro(libro3)
est2.agregar_libro(libro4)
est2.agregar_libro(libro5)
est3.agregar_libro(libro6)
est3.agregar_libro(libro7)
est3.agregar_libro(libro8)
est3.agregar_libro(libro9)
est3.agregar_libro(libro10)
for libro in est2.libros:
    print(libro.autor,libro.titulo)
    est2.contar_libros(libro.titulo,libro.autor)

