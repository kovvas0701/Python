#Hacer un programa donde se debere imprimir por la consola la palabra con mas caracteres de dos palabras dadas. En el caso que ambas tengan la misma cantidad de caracteres deban de mostrarse el mensaje son iguales.

while True:
    frase1 = input("Ingrese la primera frase: ").replace(" ","")
    print("NO PONGAS ESPACIOS")
    frase2 = input("Ingrese la segunda frase: ").replace(" ","")
    print("NO PONGAS ESPACIOS")

    counter1 = len(frase1)
    counter2 = len(frase2)


    if counter1 > counter2:
        print(f'La primera frase tiene más caracteres que la primera: {counter1} > {counter2}')
        
    elif counter1 < counter2:
        print(f'La segunda frase tiene mas caracteres que la primera: {counter1} < {counter2}')
        
    else: 
        print('Ambas frases son iguales')
        break

