import csv

def save_video_game_csv(file_path, data):
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        headers = data[0].keys()

        writer = csv.DictWriter(file, fieldnames=headers) 
        writer.writeheader()
        writer.writerows(data)

def save_video_game_tsv(file_path, data):
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        headers = data[0].keys()

        writer = csv.DictWriter(file, fieldnames=headers, delimiter="\t") 
        writer.writeheader()
        writer.writerows(data)

video_games = []

while True:
    try:
        quantity = int(input("¿Cuántos videojuegos deseas registrar?: "))
        if quantity > 0:
            break
        print("Por favor, ingresa un número mayor a cero.")
    except ValueError:
        print("Entrada inválida. Debes ingresar un número entero.")

for i in range(quantity):
    print(f"\n--- Videojuego {i + 1} de {quantity} ---")
    name = input("Nombre: ").strip()
    genre = input("Género: ").strip()
    developer = input("Desarrollador: ").strip()
    rating = input("Clasificación: ").strip()
    
    game_data = {
        "nombre": name,
        "género": genre,
        "desarrollador": developer,
        "clasificación": rating
    }
    
    video_games.append(game_data)

save_video_game_csv('video_games.csv', video_games)
save_video_game_tsv('video_games.tsv', video_games)
print("\n¡Archivos 'video_games.csv' y 'video_games.tsv' guardados con éxito!")

