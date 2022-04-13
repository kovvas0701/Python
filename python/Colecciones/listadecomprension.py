

string = 'Hola'

lista = []

for i in string:
    lista.append(i)

print(lista)

print('*****************')

lista = [x**2 for x in range(0,11)] # crear lista rapidamente del 0,11 
print(lista)

print('*****************')

celsius = [0,10,20,34,5]

faren = [((9/5)*temp + 32) for temp in celsius]

print(faren)

print('*****************')

faren = []

for temp in celsius:
    faren.append(((9/5)*temp + 32))
print(celsius)
    