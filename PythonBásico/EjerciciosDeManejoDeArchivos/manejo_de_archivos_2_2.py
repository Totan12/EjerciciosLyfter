def create_file(name_file, content):
    with open(name_file, "w" , encoding="utf-8") as file:
        file.write(content)

def count_words(name_file):
    with open(name_file, "r", encoding="utf-8") as file:
        word_list = file.read().split()
    return f"Este archivo contiene {len(word_list)} palabras"

def main():
    poem = """El agua de la acequia corre libre,
bañando las raíces del olvido,
el viento canta un verso adormecido
y el día busca un muelle donde vibre.

No pidas al reloj que se detenga
ni al pájaro que olvide su destino,
cada hoja que cae en el camino
sabe que no hay fuerza que la sostenga.

La noche llegará con sus estrellas,
dejando atrás el fuego de la tarde,
borrando del camino nuestras huellas.

Descansa la mirada en el paisaje,
no temas al silencio que resguarda,
que el alma solo viaja con su equipaje."""
    name = "archivo3.txt"
    
    create_file(name, poem)
    print(count_words(name))

if __name__ =="__main__":
    main()