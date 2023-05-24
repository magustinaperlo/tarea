#paso por acá para dejar visado los ejercicios: Excelente !
#quiero que esta funcion salude a alguien
def saludo(nombre):
    print("Hola mucho gusto", nombre)
saludo("Mariela")

#queiro que esta funcion me de la division de dos numeros
def dividir(a, b):
    print (a / b)
dividir (25, 5) #5
dividir (250, 5) #50

#quiero que esta funcion me sume 3 numeros que le voy a pedir al usuario que ingrese
def suma(a, b, c):
    suma=0
    print(a+b+c)
    suma=a+b+c
    print ("la suma es:" + str(suma))  
a=int(input("ingrese el primer numero"))
b=int(input("ingrese el segundo numero"))
c=int(input("ingrese el tercer numero"))
suma(a,b,c)

#quiero que esta funcion me diga las actividades que voy a tenes tales dias
def agenda(dia):
    lunes=""
    martes=""
    miercoles=""
    jueves=""
    viernes=""
    lista=["sop y pr2" , "mod y pp1" , "pp2 y pp1" , "map y bda" , "pp1"]
    lista2=["lunes" , "martes" , "miercoles" , "jueves" , "viernes" ]
    for i in range(0,len(lista2)):
        if (lista2[i]==dia):
            print(lista[i])
agenda(input("ingrese un dia de la semana "))


#quiero que esta funcion me permita ingresar un nombre y edad de personas
def datos_personales(nombre, edad):
    print("soy " + nombre + " " + "y " + "tengo " + edad + " " + "años ")
nombre=(input("Ingresa tu nombre: "))
edad=(input("ingresa tu edad: "))
datos_personales(nombre, edad) 

#quierooo que esta funcion me permita ingresar un nombre y edad de personas verrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
def datos_personales(nombre, edad):
    cont=0
    listanom=[]
    listaedad=[]
    while (cont<5):
        listanom.append(input("ingrese una tarea: "))
        listaedad.append(input("ingrese una fecha: "))
        cont=cont+1
    print("soy " + nombre + " " + "y " + "tengo " + edad + " " + "años ")
datos_personales(nombre, edad)
