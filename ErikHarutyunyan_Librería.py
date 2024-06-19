import time
import random

class estructLibro:
    def __init__(self, isbn: str, titulo: str, pagina: int, genero: str, retraso: bool, autor: str):
        self.isbn: str = isbn
        self.titulo: str = titulo
        self.pagina: int = pagina
        self.genero: str = genero
        self.retraso: bool = retraso
        self.autor: str = autor

    def imprimirLibro(self):
        print(f"{self.isbn}" + "\t" +f"{self.titulo}" + ", " + f"{self.genero}" + ", " + f"{self.pagina}" + " págs, " + f"{self.autor}" + ".")
    
    def getIsbn(self):
        return f"{self.isbn}"
    
    def getGenero(self):
        return f"{self.genero}"
    def getRetraso(self):
        if(self.retraso == True):
            return " con retraso"
        else:
            return ""

    

# ********************** GENERACIÓN DE LIBRO ****** INICIO ************************************

def genIsbn():
    
    isbn = []

    isbn.append(str(random.randint(978,979)))
    isbn.append("-")
    isbn.append(str(random.randint(10,99)))
    isbn.append("-")
    isbn.append(str(random.randint(10000,99999)))
    isbn.append("-")
    isbn.append(str(random.randint(10,99)))
    isbn.append("-")
    isbn.append(str(random.randint(0,9)))

    return "".join(isbn) # **** 1 ****



def genTit():
    
    # Genera un título de libro en español siguiendo la estructura:
    # # El [animal] [acciones] con [estado]
    
    titulo = ["El"]

    animales = [ # **** 2 ****
        "gorila", "chimpancé", "caballo", "perro", "gato",
        "león", "tigre", "elefante", "delfín", "camello",
        "león marino", "hipopótamo", "oso polar", "ornitorrinco",
        "zorro", "rinoceronte", "guepardo", "ratón", "topo", "jaguar"
    ]
    titulo.append(animales[random.randint(0, 19)])

    accion = [
        "trepa", "lanza", "galopea", "ladra", "afila",
        "ruge", "acecha", "destroza", "salta", "camina",
        "baila", "chapotea", "nada", "pone", "escarba",
        "carga", "corre", "roe", "excava", "vuela"
    ]
    titulo.append(accion[random.randint(0, 19)])

    titulo.append("con")
    estado = [
        "tristeza", "felicidad", "exaltación", "entusiasmo", "frialdad",
        "fuerza", "locura", "agresividad", "imparcialidad", "ira",
        "sorpresa", "desesperación", "esperanza", "euforia", "melancolía",
        "apernsión", "serenidad", "euforia", "desasosiego", "desgracia"
    ]
    titulo.append(estado[random.randint(0, 19)])

    
    return " ".join(titulo) 



def genGen():
    accion = [
        "Terror", "Fantasia", "Miedo"
    ]
    
    return accion[random.randint(0,2)]


def genRetra():
    if(random.randint(0,1) == 1):
        return True
    else:
        return False

def genAutor():
    nombre = []
   
    nomb = [
        "Juan", "María", "Carlos", "Ana", "Pedro",
        "Laura", "Diego", "Isabel", "Andrés", "Sofía",
        "Luis", "Elena", "Fernando", "Carmen", "Roberto",
        "Lucía", "Javier", "Marta", "Ricardo", "Valeria"
    ]

    nombre.append(nomb[random.randint(0, 19)])

    primer_apellido = [
        "García", "Martínez", "Rodríguez", "López", "Pérez",
        "Sánchez", "González", "Ramírez", "Torres", "Flores",
        "Hernández", "Fernández", "Gómez", "Díaz", "Muñoz",
        "Álvarez", "Romero", "Herrera", "Medina", "Castro"
    ]
    nombre.append(primer_apellido[random.randint(0, 19)])

    segundo_apellido = [
        "Ruiz", "Morales", "Jiménez", "Moreno", "Ortega",
        "Silva", "Vargas", "Rojas", "Molina", "Soto",
        "Chávez", "Gutiérrez", "Mendoza", "Delgado", "Cruz",
        "Campos", "Castillo", "Vega", "Guerrero", "Ramos"
    ]
    nombre.append(segundo_apellido[random.randint(0, 19)])
    
    return " ".join(nombre)

def checkISBN(pilaLib,lib): # **** 3 ****
    while len(pilaLib) != 0:
        if pilaLib.pop().getIsbn() == lib.getIsbn():
            return -1
    return 0


def genLib(LibrosDevueltos, Libros_Terror, Libros_Fantasia, Libros_Miedo):    
    lib = estructLibro(genIsbn(),genTit(),random.randint(10,500),genGen(),genRetra(),genAutor())
    
    # Comprobamos si se repite el ISBN
    if checkISBN(LibrosDevueltos.copy(), lib) == -1 or checkISBN(Libros_Terror.copy(), lib) == -1 or checkISBN(Libros_Fantasia.copy(), lib) == -1 or checkISBN(Libros_Miedo.copy(), lib) == -1 :
        genLib(LibrosDevueltos, Libros_Terror, Libros_Fantasia, Libros_Miedo)
    
    return lib

# ********************** GENERACIÓN DE LIBRO ****** FIN ************************************


# ********************** FUNCIONES GENERALES ************* INICIO ********************************************************

def validarNum(cad):
    try:
        cad = int(cad)
        if cad >= 8 or cad <= 0:
            print("ERROR. El número debe estar entre 1 y 7.\n")
            return None
        else:
            return cad
    except ValueError:
        print("ERROR. No se ha introducido un número.\n")
        return None

def imprimirPila(LibrosDevueltos):
    if len(LibrosDevueltos) == 0:
        print ("No se encuentran libros en esta pila")
    while len(LibrosDevueltos) != 0:
        estructLibro.imprimirLibro(LibrosDevueltos.pop())

# OPCION 1 ***************************************************************************    
def devLibAPila(LibrosDevueltos, Libros_Terror, Libros_Fantasia, Libros_Miedo):
    lib = genLib(LibrosDevueltos, Libros_Terror, Libros_Fantasia, Libros_Miedo)
    LibrosDevueltos.append(lib)
    print ("Libro devuelto correctamente: ")
    estructLibro.imprimirLibro(lib)

# OPCION 2 ***************************************************************************    
def ordLibEnGen(LibrosDevueltos, Libros_Terror, Libros_Fantasia, Libros_Miedo):
    if LibrosDevueltos:
        libr = LibrosDevueltos.pop()
        if libr.genero == "Terror":
            Libros_Terror.append(libr)
        if libr.genero == "Fantasia":
            Libros_Fantasia.append(libr)
        if libr.genero == "Miedo":
            Libros_Miedo.append(libr)
    else:
        print("No se encuentran libros en esta pila")
        return None


# OPCION 3 ***************************************************************************    
def imprPilaDev(LibrosDevueltos):
    if len(LibrosDevueltos) != 0:
        print("ISBN \t\t\tTítulo, Género, Páginas, Autor.")
        imprimirPila(LibrosDevueltos)   
    else:
        print("No se encuentran libros en esta pila")

# OPCION 4 ***************************************************************************    
def imprPilaGen(Libros_Terror, Libros_Fantasia, Libros_Miedo):
    print("Selecciona una opción:")
    print("1. Terror ")
    print("2. Fantasia ")
    print("3. Miedo ")
    num_2 = input("Introduzca el número correspondiente: ")
    
    if not num_2.isdigit():
        print("ERROR. No se ha introducido un número.\n")
        return 0
    num_2 = int(num_2)

    if num_2 >= 4 or num_2 <= 0:
        print("ERROR. El número debe estar entre 1 y 3.\n")
        return 0
    
    if num_2 == 1:
        imprimirPila(Libros_Terror)
    if num_2 == 2:
        imprimirPila(Libros_Fantasia)
    if num_2 == 3:
        imprimirPila(Libros_Miedo)
    

# OPCION 5 ***************************************************************************    
def verInfo(LibrosDevueltos):
    if LibrosDevueltos:
        print("ISBN \t\t\tTítulo, Género, Páginas, Autor.")
        estructLibro.imprimirLibro(LibrosDevueltos[-1])
    else:
        print("No se encuentran libros en esta pila")

# OPCION 6 ***************************************************************************
def imprimirPilaISBN(pilaISBN):
    cadena = ""
    while len(pilaISBN) != 0:
        cadena = f"{cadena}{"|"}{pilaISBN.pop().getIsbn()}{"| "}"
    return cadena

def imprimirTextoPila(LibrosDevueltos, Libros_Terror, Libros_Fantasia, Libros_Miedo):
    print("*******************************************************")
    print("Libros devueltos: " + imprimirPilaISBN(LibrosDevueltos.copy()) + "\n")
    print("PILA Terror: \t" + imprimirPilaISBN(Libros_Terror.copy()))
    print("PILA Fantasía:\t" + imprimirPilaISBN(Libros_Fantasia.copy()))
    print("PILA Miedo:\t" + imprimirPilaISBN(Libros_Miedo.copy()) + "\n")   
    
def closeDorToSec(Libros_Terror, Libros_Fantasia, Libros_Miedo):

    randPila = random.randint(1,3)
    if randPila == 1 and len(Libros_Terror) != 0:
        lib = Libros_Terror.pop()
    elif randPila == 2 and len(Libros_Fantasia) != 0:
        lib = Libros_Fantasia.pop()
    elif randPila == 3 and len(Libros_Miedo) != 0:
        lib = Libros_Miedo.pop()
    else:
        lib = closeDorToSec(Libros_Terror, Libros_Fantasia, Libros_Miedo)
    return lib


def startSim(LibrosDevueltos, Libros_Terror, Libros_Fantasia, Libros_Miedo): # **** 4 ****
    
    # 30 segundos 
    tiempo = 1
    while (tiempo <= 30):
        time.sleep(1)
        tiempo = tiempo + 1

        if tiempo % 2 == 0:
            lib = genLib(LibrosDevueltos, Libros_Terror, Libros_Fantasia, Libros_Miedo)
            LibrosDevueltos.append(lib)
            imprimirTextoPila(LibrosDevueltos, Libros_Terror, Libros_Fantasia, Libros_Miedo)
            
            print ("EVENTO: El libro con ISBN "+ lib.getIsbn() + " ha sido devuelto.")
            print("*******************************************************")

        if tiempo % 3 == 0: 
            lib = LibrosDevueltos.pop()
            if lib.genero == "Terror":
                Libros_Terror.append(lib)
            if lib.genero == "Fantasia":
                Libros_Fantasia.append(lib)
            if lib.genero == "Miedo":
                Libros_Miedo.append(lib)
            imprimirTextoPila(LibrosDevueltos, Libros_Terror, Libros_Fantasia, Libros_Miedo)            

            print ("EVENTO: El libro con ISBN "+ lib.getIsbn() + " ha sido ordenado en la PILA " + lib.getGenero() + lib.getRetraso() + ".")
            print("*******************************************************")

    # Puerta cerrada    
    tiempo = 1
    while (not(len(LibrosDevueltos) == 0 and len(Libros_Terror) == 0 and len(Libros_Fantasia) == 0 and len(Libros_Miedo) == 0)):
        time.sleep(1)
        tiempo = tiempo + 1
        
        if len(LibrosDevueltos) != 0:
            ordLibEnGen(LibrosDevueltos, Libros_Terror, Libros_Fantasia, Libros_Miedo)
            imprimirTextoPila(LibrosDevueltos, Libros_Terror, Libros_Fantasia, Libros_Miedo)

            print ("EVENTO: El libro con ISBN "+ lib.getIsbn() + " ha sido ordenado en la PILA " + lib.getGenero() + lib.getRetraso() + ".")
            print("*******************************************************")
        
        if tiempo % 2 == 0:
            
            lib = closeDorToSec(Libros_Terror, Libros_Fantasia, Libros_Miedo) # **** 5 ****

            imprimirTextoPila(LibrosDevueltos, Libros_Terror, Libros_Fantasia, Libros_Miedo)
            print("EVENTO: El libro con ISBN "+ lib.getIsbn() +" ha sido devuelto a su estantería.")
            print("*******************************************************")

# ********************** FUNCIONES GENERALES ****** FIN ************************************


# ********************** MAIN ********************************** INICIO ************************************************

LibrosDevueltos = []
Libros_Terror = []
Libros_Fantasia = []
Libros_Miedo = []

while(True):
    num = 0

    print("\n|************************************************************************|")
    print("| Selecciona una opción:                                                 |")
    print("| 1. Devolver un libro a la pila de LibrosDevueltos                      |")
    print("| 2. Ordenar un libro de LibrosDevueltos a su pila de género             |")
    print("| 3. Imprimir la pila LibrosDevueltos                                    |")
    print("| 4. Imprimir una de las pilas de género: 1,2,3                          |")
    print("| 5. Ver información sobre el próximo libro a ordenar de LibrosDevueltos |")
    print("| 6. Iniciar la simulación                                               |")
    print("| 7. Salir de la aplicación                                              |")
    print("|************************************************************************|\n")

    
    num = input("Introduzca el número correspondiente: ")
    
    if not num.isdigit():
        print("ERROR. No se ha introducido un número.\n")
        continue
    num = int(num)
    if num >= 8 or num <= 0:
        print("ERROR. El número debe estar entre 1 y 7.\n")
        continue

    if num == 1:
        devLibAPila(LibrosDevueltos, Libros_Terror, Libros_Fantasia, Libros_Miedo)
    elif num == 2:
        ordLibEnGen(LibrosDevueltos, Libros_Terror, Libros_Fantasia, Libros_Miedo)
    elif num == 3:
        imprPilaDev(LibrosDevueltos.copy())
    elif num == 4:
        imprPilaGen(Libros_Terror.copy(), Libros_Fantasia.copy(), Libros_Miedo.copy())
    elif num == 5:
        verInfo(LibrosDevueltos)
    elif num == 6:
        startSim(LibrosDevueltos, Libros_Terror, Libros_Fantasia, Libros_Miedo)
    elif num == 7:
        exit (0) 
    
# ********************** MAIN ****** FIN ********************************************
