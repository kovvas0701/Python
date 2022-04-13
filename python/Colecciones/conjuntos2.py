#Conjuntos


a = frozenset({1,2,3}) #A es un conjunto inmutable
b = {3,4,5}

c =a | b #Union de 2 conjuntos

print(c)

c = a & b #Inteserccion de conjuntos

print(c)

c = a - b

print(c) #Diferencia de conjuntos


c = {1,2,3,5}

print(a.issubset(c)) #A es un subconjunto del conjunto C?

print(c.issuperset(a)) #Si C es superconjunto de A

print(a.isdisjoint(b)) #Conjunto A son disconexos?


