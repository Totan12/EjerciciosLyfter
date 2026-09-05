import Student

def calculate_student_average(student):
    total = student.spanish + student.english + student.social_studies + student.science
    return total / 4

def is_valid_name(name):
    cleaned_name = name.strip()
    if not cleaned_name:
        return False
    for char in cleaned_name:
        if not (char.isalpha() or char.isspace()):
            return False
    return True

def is_valid_section(section):
    cleaned = section.strip()
    if len(cleaned) < 2 or len(cleaned) > 3:
        return False
    digits_part = cleaned[:-1]  
    letter_part = cleaned[-1]  
    return digits_part.isdigit() and letter_part.isalpha()

def student_exists(name, section, students):
    for student in students:
        if student.name.lower() == name.strip().lower() and student.section == section.strip().upper():
            return True
    return False

def get_valid_grade(subject_name):
    while True:
        try:
            grade = float(input(f"Enter {subject_name} grade (0-100): "))
            if 0 <= grade <= 100:
                return grade
            print("[Error] Grade must be between 0 and 100.")
        except ValueError:
            print("[Error] Invalid input. Please enter a valid number.")

def add_students(students):
    while True:
        print("\n--- Add New Student ---")
        
        name = input("Enter full name: ").strip()
        while not is_valid_name(name):
            print("[Error] Invalid name. It cannot be empty, contain numbers or symbols.")
            name = input("Enter full name: ").strip()
            
        section = input("Enter section (e.g., 11B): ").strip().upper()
        while not is_valid_section(section):
            print("[Error] Invalid section format. Examples: 10A, 11B, 7C.")
            section = input("Enter section (e.g., 11B): ").strip().upper()
            
        if student_exists(name, section, students):
            print(f"[Error] A student named '{name}' in section '{section}' already exists.")
            if input("Do you want to try adding another student? (y/n): ").lower() != 'y':
                break
            continue

        spanish = get_valid_grade("Spanish")
        english = get_valid_grade("English")
        social_studies = get_valid_grade("Social Studies")
        science = get_valid_grade("Science")
        
        # Se instancia la clase Student
        new_student = Student(name, section, spanish, english, social_studies, science)
        students.append(new_student)
        print(f"[Success] Student '{name}' added successfully.")
        
        if input("\nDo you want to add another student? (y/n): ").lower() != 'y':
            break

def display_all_students(students):
    if not students:
        print("\nNo students registered yet.")
        return
        
    print("\n==================== ALL STUDENTS LIST ====================")
    for idx, s in enumerate(students, 1):
        avg = calculate_student_average(s)
        print(f"{idx}. Name: {s.name} | Section: {s.section}")
        print(f"   Grades -> Spa: {s.spanish} | Eng: {s.english} | Soc: {s.social_studies} | Sci: {s.science}")
        print(f"   Average: {avg:.2f}")
        print("-" * 55)

def display_top_three(students):
    if not students:
        print("\nNo students registered to calculate Top 3.")
        return
        
    sorted_students = sorted(students, key=calculate_student_average, reverse=True)
    
    print("\n==================== TOP 3 STUDENTS ====================")
    for idx, s in enumerate(sorted_students[:3], 1):
        avg = calculate_student_average(s)
        print(f"Rank {idx}: {s.name} [Sec: {s.section}] - Average: {avg:.2f}")

def display_global_average(students):
    if not students:
        print("\nNo students registered to calculate global average.")
        return
        
    total_averages = sum(calculate_student_average(s) for s in students)
    global_avg = total_averages / len(students)
    print(f"""
=======================================================
    Global Average of all {len(students)} students: {global_avg:.2f}
=======================================================""")

def delete_student(students):
    if not students:
        print("\nNo students registered to delete.")
        return
        
    print("\n--- Delete Student ---")
    name = input("Enter the student's name to delete: ").strip()
    section = input("Enter the student's section: ").strip().upper()
    
    target_student = None
    for s in students:
        if s.name.lower() == name.lower() and s.section == section:
            target_student = s
            break
            
    if not target_student:
        print("\n[Error] Student not found with the provided name and section.")
        return
        
    confirm = input(f"Are you sure you want to delete {target_student.name} from {section}? (y/n): ").lower()
    if confirm == 'y':
        students.remove(target_student)
        print("[Success] Student deleted successfully.")
    else:
        print("[Cancelled] Deletion aborted.")

def display_failed_students(students):
    if not students:
        print("\nNo students registered yet.")
        return
        
    print("\n==================== FAILED STUDENTS REPORT ====================")
    found_failed = False
    
    subjects = [("Spanish", "spanish"), ("English", "english"), ("Social Studies", "social_studies"), ("Science", "science")]
    
    for s in students:
        failed_subjects = []
        for subject_label, attr in subjects:
            grade = getattr(s, attr)
            if grade < 60:
                failed_subjects.append(f"{subject_label}: {grade}")
                
        if failed_subjects:
            found_failed = True
            print(f"Name: {s.name} | Section: {s.section}")
            print(f"  -> Failed Subjects: {', '.join(failed_subjects)}")
            print("-" * 55)
            
    if not found_failed:
        print("Great! No students have failed any subjects.")