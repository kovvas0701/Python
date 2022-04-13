'''
and( Conjuncion ) true = 1, false = 0
True and true = true
true and false = false
false and false = false
false and false = false
or ( Disyuncion ) solo un false y es = false
True or true = true
true or false = true
false or true = true
false and false = false
not ( negacion) "LO CONTRARIO"
not(true) = false
not(false) = true
#ORDEN LOGICO
1. not
2. and
3. or
'''

A= 10
B= 12
C=13
D=10
resultado= ((A>B) or (A<C) and (A==C) or (A>=B))
print(resultado)

a=10
b=15
c=20
resultado= not((a>b) or (b<c))
print(resultado)

