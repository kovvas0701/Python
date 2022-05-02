#Realizar un juego para adivinar un numero. Para ello general un numero aleatorio entre 0-100, y luego ir pidiendo numero indicando "Es mayor" o "Es menor" segun sea mayor o menor con respecto a "x". El proceso termina cuando el usuario acierta y mostrar el numero de intentos.

import random

num = random.randint(1,100) #Crear un numero aleatorio de x al y

contador =  0 # Contador de intentos 

while True: 
    x = int(input("Digite el numero a adivinar: "))
    contador += 1 #Cada vez que se digite un "x" al contador se le sumara 1
    if x > num:
        print(f"{x} es MENOR al numero aleatorio, sigue intentado")
    elif x < num:
        print(f"{x} es MAYOR al numero, sigue intentado")
    else:
        print(f"Acertaste el numero era: {num}, y lo intentaste {contador} veces")
        break #Romper bucle

print('Alejandro')


    
    

