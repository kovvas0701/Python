#Hacer un programaque pida un numero por teclado y guarda en una lista su tabla de multplicar hasta el 10. Por ejemplo si digita el 5 tendra: 5,10,20,25 ...

name = str(input("Hola, como te llamas: "))
print(f"Hola {name}")

print("Tabla del 1 al 10, como primer ejemplo \n")

lista = list(range(1,11))

print(lista)

x = int(input("Digite un numero: "))

for i in lista:   #Lista 
    i *= x    #Los valorees de la lista se multiplican por el valor digitado por el usuario ( i = i*x) y luego se printea los valor y con guiones por el end)
    lista2 = [i]
    print(i,end="-")
    lista2 = [i]
    lista.append(lista2) #Colocar en una lista.
     
     
print(f"\n {name},definira el rango de la tabla de multiplicar, \n")


print("El primer valor sera el rango x y la segunda el rango y, por ejemplo 1 y 5, se multiplicara el numero de la tabla 1x,2x,3x,4x,5x.")

x = int(input("Seleccione el primer valor: "))
y = int(input("Seleccione el segundo valor: "))

z = int(input("La tabla se multiplicara por: "))

for i in list(range(x,y+1)):
    i *= z
    print(i,end="-") 
    