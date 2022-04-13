
num1 = int(input("Digite un numero: "))
num2 = int(input("Digite otro numero: ")) 

if num1%2==0 and num2%2==0:
    print("Ambos son pares")
elif num1%2==0 and num2%2!=0:
    print(f"{num1} es par sin embargo el {num2} no es par")
elif num1%2!=0 and num2%2==0:
    print(f"{num1} no es par, pero el {num2} si :)")
else:
    print("Ninguno numero es par")

'''
if 
elif
else
'''