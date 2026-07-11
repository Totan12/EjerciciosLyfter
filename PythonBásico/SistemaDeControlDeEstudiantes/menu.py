def print_menu():
    print(
        """
============STUDENT CONTROL SYSTEM============

            1. Add Students
            2. View All Students
            3. View Top 3 Students
            4. View Global Average
            5. Export Data to CSV
            6. Import Data from CSV
            7. Delete a Student
            8. View Failed Students
            9. Exit
===============================================
"""
    )

def get_menu_choice():
    while True:
        try:
            choice = int(input("\nPlease select a option (1-9): "))
            if 1 <= choice <=9:
                return choice
            print("[ERROR] Selection out of range. Choose between 1 and 9.")
        except ValueError:
            print("[ERROR] Invalid input. Please enter a number.")

