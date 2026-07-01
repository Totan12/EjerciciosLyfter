time = int(input("Ingrese el timepo en segundos: "))
ten_minutes = 10 * 60
if time > ten_minutes:
    print("Mayor")
elif time <ten_minutes:
    print(f"Segundos restantes: {ten_minutes - time}")
else:
    print("Igual")