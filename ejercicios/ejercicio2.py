#Llenar una lista con los numeros del 1 al 10, luego modificar los elementos de la lista multiplicandolos por un valor que el usuario digite


name = input("Hola como te llamas: ") # Nombre del usuario

print(f'Bienvenido, {name}') #bienvenida


lista = list(range(1,11)) #Creacion de la lista del 1 al 10

print(f"Lista original: {lista}") #Vista original de la lista



num = int(input(f"\n{name}, digite un numero: ")) #Pidiendole el numero al multiplicar 


for indice,i in enumerate(lista):  #Con el enumerate se puede modificar el interior de la lista | en este caso lo multiplicamos por un numero cualquier
    lista[indice] *= num #Modificando la lista
     
    
# (linea de codigo 18 al 23) ES LO MÁS IMPORTANTE DE TODO EL EJERCICIO, ENTENDERLO 
    
print(f'\nLista final con los elementos multiplicados por {num}')
print(f'{lista}')
