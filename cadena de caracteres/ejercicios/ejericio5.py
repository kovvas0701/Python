#Hacer un programa donde se cuente cada una de las vocales de una cadena, mostrar el conteo de las apareiciones de cada vocal.

cadena = input('Digite una cadena: ').lower()

a = cadena.count('a')
e = cadena.count('e')
i = cadena.count('i')
o = cadena.count('o')
u = cadena.count('u')

print(f'La cadena es {cadena}, y tiene \nVocal "a": {a},\nVocal "e": {e},\nVocal "i": {i},\nVocal "o": {o},\nVocal "u": {u}')