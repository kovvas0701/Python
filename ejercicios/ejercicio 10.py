#Hacer un programa dque pida una cadena por teclado luego meta los caracteres en una lista sin repetir caracteres.


cadena = input("Digite una palabra: ")

lista = []

for i in cadena: 
    if i not in lista: #Si el caracter por el cual vamos aun no esta en la lista, se agrega a la lista
        lista.append(i) #Se agrega el caracter a la lista
        
print(lista)
    