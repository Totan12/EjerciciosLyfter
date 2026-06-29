first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))
third = float(input("Enter the third number: "))
#====================Primera solución==============
max_number = max(first, second, third)
print(max_number)
#===================Segunda solución===============
#El float("-inf") es un menos infinito teórico para cuando se busca el valor mayor empezar con el minimo
max_num = float("-inf")
if first > max_number:
    max_num = first
if second > max_num:
    max_num = second
if third > max_num:
    max_num = third

print(max_num)