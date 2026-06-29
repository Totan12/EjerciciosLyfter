import csv

def reader_csv(file_path):
    with open(file_path, "r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        for line in reader:
            print(f"""Nombre: {line[0]}.
Género: {line[1]}.
Desarrollador: {line[2]}
Clasificación: {line[3]}
""")

reader_csv("video_games.csv")