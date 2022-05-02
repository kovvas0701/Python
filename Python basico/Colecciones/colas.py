#Colas, FIRST INPUT, primero en entrar, primero en salir

cola = ['Maria', 'Alejandro', 'Jose', 'Mario']

cola.append('Juanchi')
cola.append('Flor')

print(cola)

# Sacando elementos por el principio de la cola
n=cola.pop(0)

print(f'Se esta atendiendo a {n}')

n=cola.pop(0)
print(f'Pase {n}')
print(cola)
