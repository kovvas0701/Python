#HACER UNA CALCULADORA

simbolo= str(input("Digite el simbolo que va a realizar: ")).upper()
numero1= float(input("Digite el primer numero de la operacion: "))
numero2= float(input("Digite el segundo numero de la operacion: "))

suma1= numero1+numero2
resta1= numero1-numero2
multiplicacion1= numero1*numero2
division1= numero1/numero2

suma= "S"
resta= "R" 
multiplicacion= "M"
division= "D"


if simbolo==suma:
    print(f"\nEl resultado de su suma es {suma1}")
elif simbolo==resta:
    print(f"\nEl resultado de su resta es {resta1}")
elif simbolo==multiplicacion:
    print(f"\nEl resultado de su multplicacion es {multiplicacion1}")
elif simbolo==division:
    print(f"\nEl resultado de su division es {division1}")
else:
    print("SE HA EQUIVOCADO")
    

