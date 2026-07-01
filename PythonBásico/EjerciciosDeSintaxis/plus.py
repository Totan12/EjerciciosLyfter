number = int(input("Ingrse un número: "))
result = 0
for i in range(1, number+1):
    result += i
print(f"El resultado de sumar todos los números predecesores y el número es: {result}")