import csv
import Student

def export_to_csv(file_path, students):
    try:
        with open(file_path, "w", encoding="utf-8", newline="") as file:
            fieldnames = ["name", "section", "spanish", "english", "social_studies", "science"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            for student in students:
                # Convertimos el objeto Student a diccionario antes de escribir
                writer.writerow(student.to_dict())
            print(f"\n[SUCCESS] Data successfully exported to {file_path}.")
    except IOError as error:
        print(f"\n[ERROR] Could not write to file: {error}")

def import_from_csv(file_path):
    students = []

    try: 
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Instanciamos la clase Student desde los datos leídos
                student = Student(
                    name=row["name"], 
                    section=row["section"], 
                    spanish=float(row["spanish"]),
                    english=float(row["english"]),
                    social_studies=float(row["social_studies"]),
                    science=float(row["science"])
                )
                students.append(student)
        print(f"\n[SUCCESS] Data successfully imported from {file_path}. {len(students)} records loaded.")
        return students
    except FileNotFoundError:
        print(f"\n[WARNING] No previous data file found ({file_path}). Starting with an empty list.")
        return []
    except (IOError, ValueError) as error:
        print(f"\n[ERROR] Failed to read or parse the CSV file: {error}")
        return []