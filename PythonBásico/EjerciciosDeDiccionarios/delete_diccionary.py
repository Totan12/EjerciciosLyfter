delete_list = ["access_level" , "age"]
employee = {
    "name" : "Jonathan", 
    "email": "jonathan.castrojc01@gmail.com", 
    "access_level": 5, 
    "age": 25
}
for i in range(len(delete_list)):
    employee.pop(delete_list[i])
print(employee)