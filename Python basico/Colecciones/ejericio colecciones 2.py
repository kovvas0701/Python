#Ejercicio 2

a = [1,2,3,4,5,4,3,2,2,1,5]
b = [4,5,6,7,8,4,5,6,7,7,8]


a =set(a) #Eliminacion de elementos repetidos de a
b =set(b) #Eliminacion de elementos repetidos de b

union = a | b #lISTA DE ELEMENTOS DE LAS 2 LISTAS
soloa = a - b #LISTA DE ELEMNTOS DE LA PRIMERA LISTA PERO NO LA B
solob = b - a # LISTA DE ELEMENTOS DE B PERO NO DE A 
interseccion = a & b # LISTA DE ELEMENTOS DE AMBAS LISTAS


print(union)
print(soloa)
print(solob)
print(interseccion)







