#Pide numeros y metelos en una lista, cuando el usariao meta un 0 ya dejaremos de insertar. Por ultimo, muestra los numeros ordenados de mayor a menos (Resuelto)


lista = [] #Creacion de lista vacia

while True:  #While True 
    num = int(input("Digite un numero: ")) #Pedimos un numero al usuario para agregarlo a la lista
    if num == 0: #Si el num digitado es igual a 0, se cierra el bucle y te printea Exit
        print('Exit')
        break
    else:  #Si no es 0, se agrega a la lista 
        lista.append(num)
        print(lista)
    

lista.sort() #Ordena la lista de menor a mayor 

print(f"Lista ordenada {lista}") #Printea la lista ordenada
