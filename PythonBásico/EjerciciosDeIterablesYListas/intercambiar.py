my_list = [4, 3, 6, 1, 7]
last_number = my_list[len(my_list)-1]
first_number = my_list[0]
my_list[0] = last_number
my_list[len(my_list)-1] = first_number
print(my_list)