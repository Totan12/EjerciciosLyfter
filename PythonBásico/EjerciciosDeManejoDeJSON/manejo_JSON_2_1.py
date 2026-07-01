import json

def read_pokemon_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        pokemons_list = json.load(file)
    
    return pokemons_list

def display_pokemon_attributes(pokemons_list):
    for pokemon in pokemons_list:
        print(f"""Nombre: {pokemon["name"]}
Tipo: {pokemon["type"]}
Nivel: {pokemon["level"]}
Habilidades:    {"\n\t\t".join(pokemon["skills"])}
""")

def main():
    data = read_pokemon_file("pokemons.json")
    display_pokemon_attributes(data)

if __name__ == "__main__":
    main()
