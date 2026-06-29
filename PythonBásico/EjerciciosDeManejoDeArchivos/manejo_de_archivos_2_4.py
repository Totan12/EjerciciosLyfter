def append_file(name_file, content):
    with open(name_file, "a", encoding="utf-8") as file:
        file.write(content + "\n")
    print("El texto se agrega al final del archivo sin borrar lo anterior")

def main():
    content = input("Ingrese un texto: ")
    append_file("archivo4.txt", content)

if __name__ == "__main__":
    main()