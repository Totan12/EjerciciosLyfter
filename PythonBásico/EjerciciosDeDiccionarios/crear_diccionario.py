list_a = ["first_name", "last_name", "role"]
list_b = ["Jonathan", "Castro", "Lyfter_student"]
result_diccionary = {}
for i in range(len(list_a)):
    result_diccionary[list_a[i]] = list_b[i]
print(result_diccionary)