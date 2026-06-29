#=============Ejercicio 1===================
def print_hello():
    print("Hello ")
    print_world()

def print_world():
    print("world")
print_hello()

#==============Ejercicio 2 ==================
#########         1.1      ##########
def var_local():
    saludo = "Hola a todos"
#print(saludo) #NameError: name 'saludo' is not defined

#########         1.2      ##########
my_list = ["hola ", "a", "todos"]
def var_global():
    my_list.append("comunidad")
    print(my_list)
print(my_list) #Salida: ['hola ', 'a', 'todos']
var_global()   #Salida: ['hola ', 'a', 'todos', 'comunidad']
#podemos ver que al llamar a una variable global en la función, 
#dentro de la funcion crea una variable nueva y no modifica la varible global


#============== Ejercicio 3 ==================
def sum_list(list):
    result = 0
    for i in list:
        result += i
    return result
print(sum_list([4, 6, 2, 29]))


#============== Ejercicio 4 ==================
def reverse(mensaje):
    result = ""
    for i in mensaje[::-1]:
        result += i
    return result
print(reverse("Hola mundo"))

#============== Ejercicio 5 ==================
def count_cases(mensaje):
    uppercase_count = 0
    lowercase_count = 0

    for char in mensaje:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
    return (f"There's {uppercase_count} upper cases and {lowercase_count} lower cases")
print(count_cases("I love Nación Sushi"))

#============== Ejercicio 6 ==================
def alphabetized_words(text):
    words = text.split("-") #split es un algoritmo que divide str y al pasarle el "-" va a dividir en base a eso
    words.sort() #sort es un algoritmo de ordenamiento, se puede ordenar palabras alfabeticamente o numbers
    return ("-".join(words))
print(alphabetized_words("python-variable-funcion-computadora-monitor"))

#============== Ejercicio 7 ==================
def is_prime(number):
    if number < 2:
        return False
    d = 2
    # d*d porque solo evaluamos hasta el cuadrado del number
    while d * d <= number:
        if number % d == 0:
            return False
        d += 1
    return True

def list_prime(list):
    result = []
    for num in list:
        if is_prime(num):
            result.append(num)
    return result
print(list_prime([1, 4, 6, 7, 13, 9, 67]))
