import csv

develop = input("Ingresar un desarrollador (ej. Ubisoft): ")

def search_video_games_developer(file_path):
    with open(file_path, "r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        print(f"---Videojuegos desarrollados por {develop}---\n")   
        found = False

        for row in reader:
            if row[2].upper() == develop.upper():
                print(f"{row[0]} (Clasificación: {row[3]}, Género: {row[1]})")
                found = True
        if not found:
            print(f"No se encontraron juegos desarrollados por {develop}")

search_video_games_developer("video_games.csv")