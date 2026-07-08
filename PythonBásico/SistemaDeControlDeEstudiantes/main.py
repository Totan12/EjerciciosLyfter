import menu
import actions
import data

def main():
    students_list = []
    
    while True:
        menu.print_menu()
        choice = menu.get_menu_choice()
        
        if choice == 1:
            actions.add_students(students_list)
        elif choice == 2:
            actions.display_all_students(students_list)
        elif choice == 3:
            actions.display_top_three(students_list)
        elif choice == 4:
            actions.display_global_average(students_list)
        elif choice == 5:
            data.export_to_csv("StudentControlSystem.txt", students_list)
        elif choice == 6:
            students_list = data.import_from_csv("StudentControlSystem.txt")
        elif choice == 7:
            actions.delete_student(students_list)
        elif choice == 8:
            actions.display_failed_students(students_list)
        elif choice == 9:
            print("\nThank you for using the Student Control System. Goodbye!")
            break

if __name__ == "__main__":
    main()