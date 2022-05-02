#Funciones sin retorno de valor (Solo retorna mensajes con print)


def saludar(Nombre): #Def declarar funciones (parametros)
    print(f'Hola {Nombre}')
    
saludar('Flor') #llamar a la funcion y los parametros
saludar('Carlos')

# Tabla de multiplicar

def tabla_multiplicar(num):
    for i in range(1,11):
        print(f" {num}*{i} = {num*i}") #numero dado * el iterador que recorre todos los numeros del 1 al 10 y = num*iterador
        
tabla_multiplicar(5)
print()
tabla_multiplicar(3)
        
        
        
        