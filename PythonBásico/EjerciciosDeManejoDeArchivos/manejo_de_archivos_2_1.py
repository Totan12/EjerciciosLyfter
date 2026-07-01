def create_file(name_file, content):
    with open(name_file, "w" , encoding="utf-8") as file:
        file.write(content)

def save_and_clear(name_file):
    with open(name_file, "r", encoding="utf-8") as file:
        message_list = file.readlines()

    clear_message = []
    for i in message_list:
        clear_message.append(i.strip())
    return " ".join(clear_message)

def main():
    message = """Hola
    mundo
    esto
    es
    python"""

    name = "archivo2.txt"

    create_file(name,message)
    print(save_and_clear(name))

if __name__=="__main__":
    main()