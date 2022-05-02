#Hacer un programam donde se reemplacen todos los espacios de una cadena por asteriscords y ademas cada palabra comience por mayusuclas.

from ast import YieldFrom
from turtle import ycor


x = str(input('Digite una frase: ')).replace(' ','*')

x = x.title() # convierte a mayus todas las primeras letras de las palabra de la cadena SIEMPRE PONER ()

print(x)