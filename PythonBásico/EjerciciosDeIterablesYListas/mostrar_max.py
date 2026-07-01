my_list = []
number_max = float("-inf")
for i in range(1, 11):
    number = int(input(f"Ingrese el {i} número:  "))
    my_list.append(number)
    if number > number_max:
        number_max = number
print(my_list)
print("El más alto fue: ", number_max)