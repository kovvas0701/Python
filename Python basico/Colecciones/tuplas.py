# Tuplas, sirven para asegurarte que una vez creadas no pueden ser modificadas
#TUPLA = INMUTABLE}

tupla = (4, "Hola", 6.89, [1,2,3])
lista = list(tupla) #transformar tupla en lista

lista =[1,2,3]
#tupla= tuple(lista)  #Transformar tupla en lista.


print(tupla.index("Hola")) #te muestra el lugar donde esta el valor que especificaste

print(tupla.count(4)) #te cuenta el valor especifico

print(len(tupla)) # contar los valores

print(tupla) #(tupla[especificar el lugar ejem. (1)]), y negativo al reves

print(tupla[1:3]) #Rango que aparece en el print

print(4 in tupla) #confirmar si hay un valor en la tupla

print(lista)