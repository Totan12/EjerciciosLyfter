def greeting():
    name = input("Ingrese su nombre: ")
    if name.isdigit():
        raise ValueError("El nombre no puede ser un número")

    try:
        age = int(input("Ingrese su edad: "))
    except ValueError:
        print("Número no valido")
        return  
    print(f"Hola {name}, su edad es {age}")
greeting()

def convert_to_int(elements_list):
    print("Resultado: ")
    for element in elements_list:
        try:
            int_convert = int(element)
            print(f"\"{element}\" convertido a {int_convert}.")
        except ValueError:
            print(f"No se pudo convertir el elemento: {element}")
convert_to_int(['4','hola','10','5.2'])

def sum_values(values_list):
    result = 0
    for item in values_list:
        try:
            float_convert = float(item)
            result += float_convert
            print(f"{item} sumado correctamente.")
        except ValueError:
            print(f"Elemento inválido: {item}")
    print(f"Total de la suma: {result}")
sum_values(['10', 'manzana', '5.5', '3', 'n/a'])