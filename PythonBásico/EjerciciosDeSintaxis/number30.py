first = int(input("Ingrese un número: "))
second = int(input("Ingrese un número: "))
third = int(input("Ingrese un número: "))

plus = first + second + third
if 30 in [first, second, third] or plus == 30:
    print("Correcto")
else:
    print("Incorrecto")