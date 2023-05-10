#Tenemos una lista de Tuplas que representan ciertas características de una serie de productos.
#Cada tupla tiene 4 elementos:
#nombre del producto
#precio
#cantidad disponible
#marca
#Se desea obtener una lista de productos que cumplan con ciertas condiciones de búsqueda:
#precio máximo
#marca específica
listatuplas=("chocoblanco", 700, 10, "cofler"), ("choconegro", 600, 12, "arcor"), ("chocoaireado", 500, 13, "milka"), ("choconmani", 750, 11, "arcor")
preciomax=750
marcaespec="arcor"
listaprecio=[]
for c in listatuplas:
    if (c[1]>=preciomax and c[3]==marcaespec):
        listaprecio.append(c)
print(listaprecio)

#Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la
#longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error.
#El programa termina cuando el usuario introduce un cero.
meses=("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiempre", "Octubre", "Noviembre", "Diciembre")
cont=0
num=0
while True:
    num = int(input("Ingrese un número: "))
    if num == 0:
        break
    if (num>0 and num<=len(meses)):
        print(meses[num-1])
    else:
        print("error")

#Crea una tupla con números, pide al usuario un número por teclado e indica cuantas veces se
#repite según lo halle en la tupla que has creado.
#RESUELVE validar los ingresos del usuario. 
tuplanum=(5,4,3,6,5,4,3,5,4)

print(tuplanum)

num=(input("ingrese un numero de la tupla: "))
if (num.isdigit() == True):
    num = int(num)
    print(tuplanum.count(num))
else:
    print("input incorrecto")

#Crea una tupla con números e indica el numero con mayor valor y el que menor tenga.
tuplanum2=(40,50,60,70,80,90,30)
print("esta es la tupla: ", tuplanum2)
print("el numero mayor de esta tupla es: ", max(tuplanum2))
print("el numero menor de esta tupla es: ", min(tuplanum2))


#Crea una tupla con valores ya predefinidos del 1 al 10, pide al usuario un índice por teclado y muestra los valores de la tupla.
#RESUELVE el caso en que no exista ese índice en la tupla.
tuplanum3=(1,2,3,4,5,6,7,8,9,10)
print(tuplanum3)
num=(int(input("Ingrese el numero del indice a saber: ")))
print(tuplanum3[num])

