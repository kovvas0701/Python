# Bucle While, conocido por interminado de operaciones

import math 

num = int(input("Digite un numero: "))

while num<0: #mientras el numero es menor a 0, sale el error, en cambio si el numero mayor a 0 no entra 
    print("Error debe ser un numero positivo")
    num = int(input("Digite un numero "))
    
print(f"\nSu raiz cuadrada es: {(math.sqrt(num)):.2f}") #:.2f Decimales despues de la coma.