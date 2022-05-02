

x = input('Digite una cadena: ')

y = x.endswith('.')

if y == True: #Si la cadena finaliza con un punto
    print(f'Su frase {x}, acaba con punto.')
else: #Cas contrario
    print('No acaba con punto, muy mal.')

