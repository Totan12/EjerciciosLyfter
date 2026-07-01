#==========================
#       Ejercicio 1    
# =========================
#Esta funcion busca cuantas veces aparece un caracter dentro de un string
def search_char(text, char):
    counter = 0

    for i in text:
        if i in char:
            counter += 1
    return f"Se ha encontrado el caracter \"{char}\" en {counter} ocaciones"
#print(search_char("programacion"))

#==========================
#       Ejercicio 2
# =========================
#Filtra las palabras por cantidad de letras
def filter_by_length(word_list, length):
    result = []
    for word in word_list:
        if len(word) > length:
            result.append(word)
    return result
#print(filter_by_length(["cielo", "sol", "maravilloso", "dia"]))

#==========================
#       Ejercicio 3
# =========================
# Retorna la cantiadad de volcales en un str

def count_vocals(text):
    vocals = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    counter = 0
    for char in text:
        if char in vocals:
            counter +=1
    return counter
#print(count_vocals("Hola mundo"))
