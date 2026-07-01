import json

def read_pokemon_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        pokemons_list = json.load(file)
    return pokemons_list

def get_pokemon_type_input():
    pokemon_type = input("Ingrese el tipo de pokemon desea buscar(water,electric,fire,etc): ")
    return pokemon_type.strip().lower()

def display_pokemon_type(pokemons_list):
    pokemon_input = get_pokemon_type_input()
    found = False
    print("Buscando los pokemons que existen de ese tipo son: \n")
    for item in pokemons_list:
        pokemon_type =item["type"]
        if pokemon_type.lower() == pokemon_input:
            print(item["name"])
            found = True
    if not found:
        print("No se encontraron pokemon de ese typo.")

def main():
    data = read_pokemon_file("pokemons.json")
    print(display_pokemon_type(data))

if __name__=="__main__":
    main()