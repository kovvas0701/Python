#cadena de caracteres | METODOS (.something)


cadena = 'Hola mundo'.upper() #convierte toda la cadena a mayusucula 

print(cadena) #tambien se puede agregar en el print .upper o .lower, da el mismo efecto. #1

cadena = 'hola mundo'.lower() #cadena en minuscula

print(cadena, 'sale en minus') #2

cadena = 'hola mundo'.capitalize() #Te pone en mayus la primera letra que encuentra 
 
print(cadena) #3

cadena = 'hola mundo'.title() #se convierte a mayus la primera letra de cada palabra que tenga la cadena

print(cadena) #4

cadena = 'hola mundo'.count('o') #cuenta la cantidad de veces que aparece una letra en la cadena, cuenta un caracter especifico y hasta palabras.

print(cadena) #5

cadena = 'Hola mundo'.find('o') 
print(cadena) #6
'''
busca la letra o palabra y te da el indice que te da, LA PRIMERA QUE ENCUENTRE y con .rfind te da la ultima coincidencia que encuentre
'''
cadena = 'hola mundo'.rfind('o') 
print(cadena) #7

cadena = '1000'.isdigit() #otorga un booleano
#cadena que comprueba si solo tiene caracteres numericos o no

print(cadena) #8

cadena = 'asqT'.isalpha() #otorga un booleano
#comprueba si solo hay caracteres alfabeticos.

print(cadena) #9

cadena = 'hola mundo'.islower() #comprueba si la cadena solo tiene caracteres minusculas

print(cadena) #10

cadena = 'Hola Mundo'.istitle() #comprueba si se sigue el metodo .title

print(cadena) #11

cadena = 'hola mundo'.isupper() #comprueba si la cadena solo tiene caracteres mayusculas

print(cadena) #12