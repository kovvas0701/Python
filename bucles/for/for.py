# Bucle For, numero determinado de iteraciones (cuantos elementos tengas en tu coleccion)
# Recorre elemento por elemento

#lista
for i in [1,2,3,4,'Alejandro']: #Nombre de iterador, in [Coleccion]
    print(f"{i}")
    

print("\n***************** \n")
    
#diccionario

diccionario = {'Alejandro': 20, 'Juan' : 20, 'Fati': 15}
     
for clave,valor in diccionario.items(): #Con .items recorres todo el diccionario. 
    print(f"{clave} -> {valor}")
    
print("\n***************** \n")

cadenas = 'Alejandro' #lector de cadenas, tira letra por letra el ciclo for, CARACTER POR CARACTER 
 
for i in cadenas:
    print(f"{i}", end = " ")  # con el end, ya no da el salto de linea.
    
for i in range(10): #crea una ista con el numero que le pongas al range
    print(f"{i}")
