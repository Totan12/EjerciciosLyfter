import json

def read_pokemon_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        pokemons_list = json.load(file)
    return pokemons_list

def display_pokemon_stats(pokemon_list):
    for pokemon in pokemon_list:
        print(
            f"""Nombre: {pokemon["name"]}
Puntos de salud: {pokemon["stats"]["hp"]}
Ataque: {pokemon["stats"]["attack"]}
Defensa: {pokemon["stats"]["defense"]}
Ataque especial: {pokemon["stats"]["sp_attack"]}
Defensa especial: {pokemon["stats"]["sp_defense"]}
Velocidad: {pokemon["stats"]["speed"]}
"""
        )

def main():
    data = read_pokemon_file("pokemons.json")
    display_pokemon_stats(data)

if __name__=="__main__":
    main()