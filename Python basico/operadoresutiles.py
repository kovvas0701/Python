lista = [1,2,3]

for i in range(10): #RANGE = RANGO DEL 0 AL NUMERO QUE PONGA EN ESTE CASO 10
    print(i)

print('******************')

print(list(range(0,11,5))) 
# DEL 0,X, EN CUANTOS PASOS
#POR EJEMPLO DE 2 EN 2 DE 5 EN 5 ETC
print('******************')
contador = 0
palabra ='Alejandro'

for a,i in enumerate(palabra): #Cuenta el numero de digitos que hay en tu variable
    print(f"{i},{a}")


print(list(range(10)))