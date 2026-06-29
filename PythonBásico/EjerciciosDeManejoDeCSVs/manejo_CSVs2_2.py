import csv

search_query = input("Ingrese la clasificación ESRB que busca (ej. T, M): ").strip()

def search_by_esrb_rating(file_path):

    with open(file_path, 'r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file)
        next(reader)
        
        print(f"\n--- Videojuegos con clasificación {search_query.upper()} ---\n")
        found = False
        
        for row in reader:
            if row[3].upper() == search_query.upper():
                print(f"""Nombre: {row[0]}.
Género: {row[1]}.
Desarrollador: {row[2]}
Clasificación: {row[3]}
""")
                print("-" * 30)
                found = True
                
        if not found:
            print("No se encontraron videojuegos con esa clasificación.")
search_by_esrb_rating("video_games.csv")