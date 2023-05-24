import random

#quiero que esta funcion me imprima un mensaje
def mensaje():
    print("Hoy va a ser un gran dia!!! ")
mensaje()
    
#quiero que esta funcion me imprima el promedio de dos numeros 
def prom():
    lista=[]
    cont=0
    suma=0
    prom=0
    while (cont<2):
        num= random.randint(1,100)
        lista.append(num)
        cont=cont + 1
    print("los numeros son: " + str(lista))
    for i in range(0, len(lista)):
        suma=suma+lista[i]
        prom=suma/cont
    print("el promedio de estos numeros es:" + str(prom))
prom()

#quiero que esta funcion me permita agendar fechas y tareas a realizar
def agenda():
    listatarea=[]
    listafechas=[]
    bandera=True
    while (bandera==True): #no hace falta el "==True" porque ya asignaste el valor a la bandera , cuando cambie de valor se corta el ciclo
        listatarea.append(input("ingrese una tarea: "))
        listafechas.append(input("ingrese una fecha: "))
        opcion= input("¿quiere ingresar mas tareas?")
        if (opcion=="no"):
            bandera=False
    for i in range (0,len(listatarea)):
        print(listatarea[i] + " - " + listafechas[i])
agenda ()

#quiero que esta funcion me genere numeros aleatorios, se almacenen y se sumen entre si
def sumalista():
    lista=[]
    num=0
    cont=0
    suma=0
    while (cont<10):
        num= random.randint(1,100)
        lista.append(num)
        cont=cont+1
    print (lista)
    for i in range (0,len(lista)):
        suma= suma+lista[i]
    print("la suma de toda la lista es: " + str(suma))
sumalista()

#quiero que esta funcion me tira un numero de un dado
def tirar_un_dado():
    num=random.randint(1,6)
    print ("el numero del dado es: " + str(num))
tirar_un_dado()
