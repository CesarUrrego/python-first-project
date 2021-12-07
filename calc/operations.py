# Suma de dos numeros
def sum_two_number(n_first, n_second):
    print("El resultado de la suma es " + str(n_first + n_second))


# Resta de dos numeros
def rest_two_number(n_first, n_second):
    print("El resultado de la suma es " + str(n_first - n_second))


# Multi de dos numeros
def mult_two_number(n_first, n_second):
    print("El resultado de la suma es " + str(n_first * n_second))


# Division de dos numeros
def div_two_number(n_first, n_second):
    if n_first == 0:
        print("no se puede dividir entre 0")
    else:
        result = n_first / n_second
        print("El resultado de la division es " + str(result))
