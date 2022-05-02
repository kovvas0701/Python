#Tipos de cadena de caracteres

cadena = 'hola mundo'.startswith('hola') #comprueba si la cadena empieza con una palabra o letra
#starwith = comienza con "palabra"
 
print(cadena) #13 #boolean

cadena = 'hola mundo'.endswith("Mundo") #comprueba si la cadena termina con una palabra o letra
#endwith = termina con "palabra"

print(cadena) #14 #boolean

cadena = "hola mundo".split() #separa la cadena por espacios (siempre y cuando este vacio) y los colaca en una lista (por lo que quieras separar ejm: '-')
#split = te otorga una lista con los elementos separados por espacios.

print(cadena) #15 #lista

cadena = ','.join('Alejandro') #junta los elementos de una lista en una cadena, y lo separa con que este en la cadena, ya sea una coma un punto o un guion o un espacio

print(cadena) #16 #cadena

cadena = '         hola          '.strip() #elimina los espacios en blanco al inicio y al final de la cadena ( ya sea espacio o lo que le otorguemos, por ejemplo ......, -----, ',,,,,,')

print(cadena) #17 #cadena libre de lo que le pasemos

cadena='Hola mundo'.replace('Hola', 'Adios') #reemplaza una palabra o letra por otra, en este caso reemplaza la palabra Hola por Adios. ("Lo que esta en la cadena, por lo que se reemplazaria")

print(cadena) #18 #cadena