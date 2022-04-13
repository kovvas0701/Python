#CAJERO AUTOMATICO con bucle 


d= 1000

while True: #Siempre poner el bucle en la linea que quieras que se repita el codigo 
    print(f"Hola, *Ustede tiene 1000* \n 1. INGRESAR DINERO \n 2. RETIRAR DINERO \n 3. MOSTRAR DINERO \n 4. SALIR")
    dinero = float(input("Seleccione --> "))

    if dinero==1:
        extra = float(input(f"Cuanto dinero quiere ingresar: "))
        d += extra
        print(f"Ahora usted tiene {d}$")        
    elif dinero==2:
        extra = float(input(f"Cuanto dinero quiere retirar: "))
        d -= extra
        print(f"Usted ahora tiene: {d}$")
    elif dinero==3:
        print(f"Usted tiene {d}$")
    elif dinero==4:
        print(f"*A D I O S*")
        break
    else:
        for i in range(1,10):
            print("*ERROR*")
        
    
