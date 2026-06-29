def create_file(name_file, content):
    with open(name_file, "w", encoding="utf-8") as file:
        file.write(content)
def save_and_upper(name_file):
    with open(name_file, "r", encoding="utf-8") as file:
        lines_list = file.readlines()
        upper_list= []
        for line in lines_list:
            upper_list.append(line.strip().upper())
    return upper_list

def create_upper_file(file_name, content_list):
    with open(file_name, "w", encoding="utf-8") as file:
        for item in content_list:
            file.write(item + "\n")
    
def main():
    name_file = "archivo3.txt"
    name_upper_file = "archivo3_upper.txt"
    content = """hola mundo
esto es python"""
    create_file(name_file, content)
    content_list = save_and_upper(name_file)
    create_upper_file(name_upper_file,content_list)

if __name__=="__main__":
    main()
