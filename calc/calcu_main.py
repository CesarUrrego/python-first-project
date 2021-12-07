import operations


# Imprimir mensaje de bienvenida
def print_welcome_message():
    print("Calculadora")
    print("Aquí puede realizar operaciones matematicas basicas")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")


# Solicita numero al usuario
def request_user_option():
    print("Ingrese una opcion del menu")
    return int(input())


def calculator(option):
    print("Ingrese el numero uno")
    number_first = float(input())
    print("Ingrese el numero dos")
    number_second = float(input())

    if option == 1:
        operations.sum_two_number(number_first, number_second)
    elif option == 2:
        operations.rest_two_number(number_first, number_second)
    elif option == 3:
        operations.mult_two_number(number_first, number_second)
    elif option == 4:
        operations.div_two_number(number_first, number_second)
    else:
        print("Fin.")


def run_program():
    print_welcome_message()
    user_option = request_user_option()

    if (user_option >= 1) and (user_option <= 4):
        calculator(user_option)
    else:
        print("Opción invalida! Intenta de nuevo.")


run_program()

