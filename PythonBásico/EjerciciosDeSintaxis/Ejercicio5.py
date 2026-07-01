grades_count = int(input("Enter the number of grades to calculate: "))
passed_grades = 0
failed_grades = 0
average_calc = 0
passed_average = 0
failed_average = 0

for i in range(grades_count):
    grade = float(input(f"Enter the {i+1} grade: "))
    if grade >= 70:
        passed_grades += 1
        passed_average += grade
        average_calc += grade
    else:
        failed_grades += 1
        failed_average += grade
        average_calc += grade

if passed_grades == 0:
    passed_average = "No students passed."
else:
    passed_average /= passed_grades

if failed_grades == 0:
    failed_average = "All students passed."
else:
    failed_average /= failed_grades

average_calc /= grades_count

print("======================================")
print(f"Passed grades: {passed_grades}")
print(f"Failed grades: {failed_grades}")
print(f"Passed average: {passed_average}")
print(f"Failed average: {failed_average}")
print(f"Average: {average_calc}")
print("=======================================")

