# Ejercicio 1
def dividir_numeros(num1, num2):
    try:
        resultado = num1 / num2
        return resultado
    except ZeroDivisionError:
        print("Error: No se puede dividir con el número cero")


print(dividir_numeros(5, 0))
print(dividir_numeros(5, 2))


# Ejercicio 2
def convertir_cadena(cadena):
    try:
        numero = int(cadena)
        return numero
    except ValueError:
        print("Error: No se puede convertir la cadena a un número entero")


print(convertir_cadena("123"))
print(convertir_cadena("abc"))

# Ejercicio 3
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Error: Fichero no encontrado.")

read_file("archivo.txt")

# Ejercicio 4
def multiples_operaciones(num1, num2):
    try:
        print(f"Suma: {num1 + num2}")
        print(f"Resta: {num1 - num2}")
        print(f"MultiplicaciÃ³n: {num1 * num2}")
        print(f"DivisiÃ³n: {num1 / num2}")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    else:
        print("Operaciones realizadas correctamente.")
    finally:
        print("Fin de las operaciones.")


multiples_operaciones(5, 0)


# Ejercicio 5
def edad_usuario(edad):
    try:
        age = int(input("Introduce tu edad: "))
        if age <= 0:
            raise ValueError("La edad debe ser un entero positivo.")
        return age
    except ValueError as e:
        print(f"Error: {e}")
    
# Ejercicio 6
def access_list_element(list, index):
    try:
        return list[index]
    except IndexError:
        print("Error: Ãndice fuera de rango.")

# Ejercicio 7
def handle_multiple_exceptions(num1, num2):
    try:
        result = num1 / num2
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    except ValueError:
        print("Error: Valor invÃ¡lido.")
    except TypeError:
        print("Error: Tipo no compatible.")

handle_multiple_exceptions(5, 1)
handle_multiple_exceptions("5", 2)
handle_multiple_exceptions(5, "2")

# Ejercicio 8
class InsufficientFundsError(Exception):
    pass

def simulate_transaction(balance, withdrawal_amount):
    try:
        if withdrawal_amount > balance:
            raise InsufficientFundsError(
                "Saldo insuficiente para la transacciÃ³n.")
        balance -= withdrawal_amount
        print(f"TransacciÃ³n realizada correctamente. Nuevo saldo: {balance}")
    except InsufficientFundsError as e:
        print(f"Error: {e}")


# Ejercicio 9

def convert_list_to_integers(list):
    integers = []
    for string in list:
        try:
            integers.append(int(string))
        except ValueError:
            print(f"Error: '{string}' no se puede transformar en un entero.")
    return integers

list2 = ["1", "2", "3", "sss", "5"]
print(convert_list_to_integers(list2))


# Ejercicio 10
def calcular_raiz_cuadrada(numero):
    try:
        if numero < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
        resultado = numero ** 0.5
        return print(f"La raíz cuadrada de {numero} es {resultado}")
    except ValueError as e:
        print(f"Error: {e}")

calcular_raiz_cuadrada(4)
calcular_raiz_cuadrada(-1)