#Programa CRUD con funcion de guardado en fichero


#Declaracion
lista=[]

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

'''Función copia de seguridad, se encarga de copiar el contenido de la
    lista en u fichero .txt 
'''
def GuardarLista():
    archivo = open("C:\\Users\\fonsi\\Desktop\\ESTUDIO\\IMF 2\\DESARROLLO DE INTERFACES\\Practicas\\Practica4DI\\CopiaSeguridad.txt",'a')
    archivo.write('\n'.join(map(str,lista)))
    archivo.close()

'''Función leer copia de seguridad, se encarga de leer el contenido del fichero
    .txt 
'''
def LeerLista():
    archivo = open("C:\\Users\\fonsi\\Desktop\\ESTUDIO\\IMF 2\\DESARROLLO DE INTERFACES\\Practicas\\Practica4DI\\CopiaSeguridad.txt",'r')         
    lineas = archivo.readlines()
    for i in range(0,len(lineas)):
        print(lineas[i])
    archivo.close()
#Bucle para que se pueda introducir los datos que se quieran
while True:
    print("Introduce una opcion\n1-Insertar\n2-Modificar\n3-Eliminar\n4-Buscar\n5-CopiaSeguridad\n6-LeerCopia\n7-Salir")
    opcion = int(input())
    if opcion == 1:
        Insertar()
    elif opcion == 2:
        Modificar()
    elif opcion == 3:
        Eliminar(input("¿Que pelicula desea eliminar?"))
    elif opcion == 4:
        Buscar(input("¿Que pelicula desea buscar?"))
    elif opcion == 5:
        GuardarLista()
    elif opcion == 6:
        LeerLista()
    else:
        break      
        
    
    
