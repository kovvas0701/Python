#Hacer un programa que determine si una palabra o frase es palindroma o no.

import time

cadena = input('Digite una cadena: ')
print(' ')
#Primero quitamos los espacios en blanco
cadena = cadena.replace(' ',"") #QUITA LOS ESPACIOS, LOS REMPLAZA POR NADA

#Invertimos cadena

cadena2 = cadena[::-1] # [::-1] es la cadena invertida #LO MÁS IMPORTANTE DE TODO EL CODIGO PARA REVERTIR LA CADENA

print(f'La cadena orignal {cadena} y la cadena invertida es {cadena2}')
print(' ')
time.sleep(2) #Espera de 2 segundos
print(' ')
if cadena == cadena2:
    print('Es palindromo')
else: 
    print('Las cadenas no son iguales')