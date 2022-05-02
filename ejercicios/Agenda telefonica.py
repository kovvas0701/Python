'''
Hacer un programa que simule una agenda de contactos. Crear un diccionario donde la clave sea el nombre del usuario y el valor sea el telefono
1. nuevo contacto
2. borrar contacto
3. ver contactos existentes
4. salir
'''
import time

Agenda = {}

while True:
    print(' ')
    print('**Menu**')
    print('1. Nuevo contacto')
    print('2. Borrar contacto')
    print('3. Ver contactos existentes')
    print('4. Salir')
    print(' ')
    
    menu = int(input("Seleccione una opcion: "))
    
    if menu == 1:
        print(' ')
        usuario = input("Digite su usuario: ")
        print(' ')
        telefono = input("Digite su telefono: ") 
        
        if usuario not in Agenda:
            Agenda[usuario] = telefono 
            print('Contacto agregado\n')
            print(' ')
            print(Agenda)
        else:
            ('El usuario ya fue agregado a la Agenda')
    
    elif menu == 2:
        print(' ')
        clean = input("Digite el usuario que desea borrar: ")
        if  usuario not in Agenda:
            print(' ')
            print("El usuario no existe")
        else:
            del(Agenda[clean])
            print(' ')
            print('Contacto eliminado con exito\n')
            print(f"Ahora sus contactos son: {Agenda}")
            
    elif menu == 3:
        print('Agenda de contactos')
        for usuario,numero in Agenda.items():
            time.sleep(2)
            print(' ')
            print(f"Nombre: {usuario}, Telefono: {numero}")
    
    else: 
        print('Hasta la proxima usuario')
        break
        
