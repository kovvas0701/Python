
a = int(input("Digite su numero: "))
b = int(input("Digite su numero: "))
c = int(input("Digite su numero: "))

if a>b and a>c:
    print(f"{a} es mayor a {b} y {c} ")
elif b>a and b>c:
    print(f"{b} es mayor {a} y {c} ")
elif c>b and c>a:
    print(f"{c} es mayor a {a} y {b}")
