
#Diccionarios   # CLAVE : VALOR

diccionario = {"azul" : "blue", "rojo" : "red", "verde" : "green" } 

diccionario["amarillo"] = "yellow" #agregar elemento al diccionario
diccionario["azul"] = "BLUE" #Modificar valor del diccionario

del(diccionario["verde"]) #Eliminar claves especificas 

print(diccionario["rojo"]) # [] te muestra el valor de la clave

print(diccionario)


diccionario = {"Alejandro":{"edad": 17, "estatura":1.79},  "Jose":[21,1.89]} #CLAVE:VALOR, se pueden colocar LISTAS y TUPLAS

print(diccionario["Alejandro"]) #Especificar la CLAVE:VALOR que quiero usar