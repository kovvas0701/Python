#HACER UN COSO QUE DIGA SI ES UNA VOCAL O NO

vocal1= input("Digite su letra: ").lower()
vocal = "a" or "e" or "i" or "u" or "o"

if vocal1==vocal:
    print(f"Su letra {vocal1}, es una vocal")
elif vocal1!=vocal:
    print(f"Su letra {vocal1}, no es una vocal, es una consonante")
elif vocal1== float:
    print("ES UN NUERO")

