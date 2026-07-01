
first_list = ["Hay", "en", "que", "iteracion", "indices", "muy"]
second_list = ["casos", "los", "la", "por", "es", "util"]
result = []

for i in range(len(first_list)):
    result.append(first_list[i])
    result.append(second_list[i])
#" ".join() es para unir los valores de una lista
print(" ".join(result))