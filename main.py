import threading
from queue import Queue

# Declaro las variables generales
texto = ""
terminamos = False
lock = threading.Lock()
lista = Queue()

# Creacion de la funcion agregarParte1 que coje el texto y mete en lista la primera mitad
def agregarParte1(texto):
    mitad = len(texto) // 2
    parte1 = texto[:mitad]
    lista.put(parte1)

# Creacion de la funcion agregarParte1 que coje el texto y mete en lista la segunda mitad
def agregarParte2(texto):
    mitad = len(texto) // 2
    parte2 = texto[mitad:]
    lista.put(parte2)

# Creacion de la funcion escritura que escribe el texto total por pantalla mostrandolo al usuario
def escritura():
    textoReserva = ""
    while terminamos == False:
        if not lista.empty():
            textoReserva = textoReserva + lista.get()
            print("Texto agregado: "+textoReserva)

#Creacion del hilo que ejecuta la funcion escritura
hiloEscritura = threading.Thread(target=escritura,)
hiloEscritura.start()

# while que se ejecuta hasta que el usuario ponga -1
while terminamos == False:

    # muestro por pantalla las instrucciones de uso para guiar al usuario
    print("Introduce un texto, -1 corta la ejecucion")

    # Recojo la informacion introducida por el usuario
    texto = input()

    # comprueba que el usuario haya puesto -1, en cuyo caso pone en true el booleano terminamos y esto proboca el fin del bucle while
    if(texto != "-1"):

        #Creacion de los hilos que ejecutan las funciones agregarParte1 y agregarParte2
        hiloAgregarParte1 = threading.Thread(target=agregarParte1, args=(texto,))
        hiloAgregarParte2 = threading.Thread(target=agregarParte2, args=(texto,))
        hiloAgregarParte1.start()
        hiloAgregarParte2.start()
    else:
        terminamos = True