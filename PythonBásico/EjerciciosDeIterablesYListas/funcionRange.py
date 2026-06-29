my_string = "Pizza con piña"
############solucion 1###############
for i in my_string[::-1]:
    print(i)
#############Solución 2###############
for i in range(len(my_string)-1, -1 ,-1):
    print(my_string[i])