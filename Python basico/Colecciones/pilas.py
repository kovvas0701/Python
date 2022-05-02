#Pilas SIGUE UNA SECUENCIA, NO SE PUEDE SACAR UN VALOR ANTES QUE OTRO


pila = [1,2,3]

#Agregando un elemento por el final
pila.append(4)
pila.append(5)

#Eliminar el ultimo elemento de la pila
pila.pop()

print(pila)

#Sacando elementos por el final

variable = pila.pop()
print(f"Sacando el elemento {variable}") #Y te muestra el ultimo elemento que encuentra


