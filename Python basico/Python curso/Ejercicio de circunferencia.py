#Area y logitud de una circunferencia

import math

a=float(input("Digite el radio de la circunferencia: "))
area= math.pi* a**2
longitud= 2*math.pi*a

# {variable:2f} 2= es la cantidad de decimales que quiero que aparezcan

print(f"Esta es el area {area:.2f} y esta la longitud {longitud:.2f}")