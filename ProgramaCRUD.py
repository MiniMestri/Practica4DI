#Programa CRUD con funcion de guardado en fichero

#Declaracion
lista=[]
condicion = True


#Funcion para insertar dato
def Insertar():
    lista.append([input("Introduzca el nombre de la pelicula: "),
                     input("Introzuca la fecha: "),
                     input("Introduzca una valoracion: ")])
#Funcion modificar datos
def Modificar():
    Eliminar(input("Que pelicula desea modificar"))
    Insertar()

#Funcion Eliminar dato
def Eliminar(nombre):
    del lista[Buscar(nombre)]

#Funcion buscar dato con retorno de posicion
def Buscar(nombre):
    encontrado = False
    i=0
    while i < len(lista) or encontrado:
        if lista[i][0] == nombre:
            encontrado = True
            print(lista[i])
            break
        else:
            i+=1
    return i
               
#Bucle para que se pueda introducir los datos que se quieran
while condicion:
    respuesta="s"
    if respuesta == "n":
        condicion = False
        
    else:
        print("Introduce una opcion\n1-Insertar\n2-Modificar\n3-Eliminar\n4-Buscar\n5-Salir")
        opcion = int(input())
        if opcion == 1:
            Insertar()
        elif opcion == 2:
            Modificar()
        elif opcion == 3:
            Eliminar(input())
        elif opcion == 4:
            Buscar(input("¿Que pelicula desea buscar"))
        else:
            break      
        
    
    
