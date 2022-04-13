#Diccionario

futbol = {10: "Ansu Fati", 30: "Gavi", 1: "Ter Steguen", 19:"Kun Agüero"}
#futbol[9] = "Memphis Depay"

print(futbol.get(9, "\nNO EXISTE")) # TOMA SOLO UN VALOR DEL DICCCIONARIO

print( 10 in futbol)

print(futbol.keys()) #Solo mostrar las claves de mi diccionario
print(futbol.values()) #Solo mostrar los valores de mi diccionario
print(futbol.items()) #Pone dentro de tuplas la clave y valor de cada elemento del diccionario
print(len(futbol)) #muestra cuantos elementos hay en el diccionario

futbol.clear() #Limpiar un diccionario
print(futbol)



