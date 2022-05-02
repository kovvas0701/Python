#Ejercicio 9, mostrar frase sin espacios y contar

frase = input("Ingrese una frase: ")    
frase2 = ''

'''
Se aplica el bucle for para recorrer la frase y lograr quitarle los espacios
i recorre toda la frase y al ver que i no es igual a espacio se guarda en la variable frase2
'''

#Quitar los espacios de la frase
for i in frase:  
   if i!=' ': 
        frase2 += i #todo lo que esta en i se une a frase 2 y serian lo mismo 
        
frase = frase2

print(frase2)
 
print(len(frase2)) #se cuenta y se printea
