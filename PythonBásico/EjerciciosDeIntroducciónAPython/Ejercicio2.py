name = input("Enter your name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))

if age <= 2:
    stage = "a baby"
elif age <= 9:
    stage = "a child"
elif age <= 12:
    stage = "a preteen"
elif age <= 17:
    stage = "a teenager"
elif age <= 39:
    stage = "a young adult"
elif age <= 59:
    stage = "an adult"   
else:
    stage = "a senior"
print(f"{name} {last_name} is {stage}")