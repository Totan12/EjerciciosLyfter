import json

def read_pokemon_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        pokemon_list = json.load(file)
    return pokemon_list

def clean_pokemon_skills(skills_text):
    clean_list = []
    raw_elements = skills_text.split(",")

    for item in raw_elements:
        clean_item = item.strip()

        if clean_item != "":
            clean_list.append(clean_item)
    return clean_list

def request_pokemon_data():
    print("--- AGREGAR NUEVO POKEMON ---")
    name = input("Nombre: ")
    pokemon_type = input("Tipo: ")
    level = int(input("Nivel: "))
    weight_kg = float(input("Peso (kg): "))

    shiny_input = input("¿Es shiny? (s/n):  ")
    shiny_input = shiny_input.strip().lower()
    if shiny_input == "s":
        is_shiny = True
    else:
        is_shiny = False

    held_item = input("Objeto equipado (deja vacío si no tiene):  ")
    held_item = held_item.strip()
    if held_item == "":
        held_item = None

    skill_input = input("Habilidades (separadas por comas):  ")
    skills = clean_pokemon_skills(skill_input)

    print("Introduce las estadisticas:")
    stats = {}
    stats["hp"] = int(input("HP: "))
    stats["attack"] = int(input("Attack: "))
    stats["defense"] = int(input("Defense: "))
    stats["sp_attack"] = int(input("Sp. Attack: "))
    stats["sp_defense"] = int(input("Sp. Defense: "))
    stats["speed"] = int(input("Speed: "))

    new_pokemon = {
        "name": name,
        "type": pokemon_type,
        "level": level,
        "weigth_kg": weight_kg,
        "is_shiny": is_shiny,
        "held_item": held_item,
        "skills": skills, 
        "stats": stats,
    }

    return new_pokemon

def save_pokemon_file(file_path, update_list):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(update_list, file, indent=4, ensure_ascii=False)

def run_main_program():
    current_data = read_pokemon_file("pokemons.json")
    new_entry = request_pokemon_data()
    current_data.append(new_entry)
    save_pokemon_file("pokemons.json", current_data)

    print(f"\n{new_entry["name"]} ha sido agregado y guardado con éxito.")

run_main_program()