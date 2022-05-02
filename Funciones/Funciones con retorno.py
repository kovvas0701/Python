#Funciones con retorno de valor

from audioop import mul


def multiplicacion(num,num2): #Def nombre(parametros)
    mult = num*num2 #multiplicacion
    return mult #Retorna el valor de la variable declara en la linea 7 PERO TAMBIEN PUEDE RETORNAR VARIOS VALORES

print(multiplicacion(3,4)) 
print(multiplicacion(9,10))

'''
Se imprime directamente con un print o se crea una nueva variable y luego se imprime la funcion
'''

mult = multiplicacion(3,4)

print(mult)
