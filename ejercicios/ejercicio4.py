#Hacer un programa para sumar numeros pares dentor de un rango.

x = int(input("Digitar un numoero para el x del range: ")) #Pedir primer valor para el range (x)
y = int(input("Digitar un numero para el y del range: " ))
# Segundo valor para el range
lista = list(range(x,y+1)) #se coloca los valores digitados en el range (x,y+1( y + 1 para que sea exacto))

suma = 0 # igual 0 para leer todo el bucle for

for i in lista: 
    if i % 2 == 0: #Si hay un valor con residuo igual divido entre 2 con residuo 0, es par, y se suma 
        suma += i #Los valores puesto en el range se le van sumando a la suma


print(f"La suma es {suma}") #Y luego la suma de todo.


