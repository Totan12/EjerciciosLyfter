import json

def read_pokemon_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        pokemons_list = json.load(file)
    return pokemons_list

def group_by_type(pokemon_list):
    group = {}
    for pokemon in pokemon_list:

        pokemon_type = pokemon["type"]
        pokemon_level = pokemon["level"]

        if pokemon_type not in group:
            group[pokemon_type] = []
            group[pokemon_type].append(pokemon_level)
    return group

def show_average(group_by_type):
    for p_type, p_level in group_by_type.items():
        if p_level: 
            average = sum(p_level) / len(p_level)
            print(f"Tipo: {p_type} -> Promedio de nivel: {average:.1f}") #El .1f es para redondear a un decimal

def main():
    data = read_pokemon_file("pokemons.json")
    group_type = group_by_type(data)
    show_average(group_type)

if __name__=="__main__":
    main()