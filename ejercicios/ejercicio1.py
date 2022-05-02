#Llenar una lista del 1 al 50, y los elementos deben mostrarse al 1-2-3-4- ... 50. (RESUELTO)

for i in range(1,51):
    print(i,end="-")


print("\n con una lista ya creada antes")

#Agregar elementos a una lista 

lista = list(range(1,51))

for i in lista:
    print(i,end="--")