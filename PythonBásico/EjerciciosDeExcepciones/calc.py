def show_menu(current_number):
    print(
        f"""
--- VALOR ACTUAL: {round(current_number, 3)} ---
1. SUMA
2. RESTA
3. MULTIPLICACIÓN 
4. DIVISIÓN 
5. BORRAR RESULTADO
6. SALIR"""
    )

def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Error: Entrada inválida. Debe ingresar un número válido.")

def run_calculator():
    current_number = 0.0

    while True:
        show_menu(current_number)
        user_choice = input("Seleccione una opción: ").strip()

        try:
            match user_choice:
                case "1":
                    new_number = get_number(
                        "Ingrese el número a sumar: "
                    )
                    current_number += new_number

                case "2":
                    new_number = get_number(
                        "Ingrese el número a restar: "
                    )
                    current_number -= new_number

                case "3":
                    new_number = get_number(
                        "Ingrese el número a multiplicar: "
                    )
                    current_number *= new_number

                case "4":
                    new_number = get_number(
                        "Ingrese el número a dividir: "
                    )
                    if new_number == 0:
                        raise ZeroDivisionError(
                            "No se puede dividir entre cero."
                        )
                    current_number /= new_number

                case "5":
                    current_number = 0.0
                    print("Resultado borrado. El valor actual es 0.0")

                case "6":
                    print("Saliendo de la calculadora. ¡Hasta luego!")
                    break

                case _:
                    raise ValueError(
                        "Opción no válida. Elija un número del 1 al 6."
                    )

        except ZeroDivisionError as error:
            print(f"Error Matemático: {error}")
        except ValueError as error:
            print(f"Error de Selección: {error}")
        except Exception as error:
            print(f"Ocurrió un error inesperado: {error}")


if __name__ == "__main__":
    run_calculator()

