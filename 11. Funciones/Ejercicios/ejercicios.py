#Ejercicio 1

def personalized_greeting(name = "desconocido"):
    print(f"Hola, {name}")

personalized_greeting("Juan")
personalized_greeting()

#Ejercicio 2
def multiply(number1, number2):
    return number1 * number2

result = multiply(5, 5)
print(result)


#Ejercicio 3
def is_even (number):
    if number % 2 == 0:
        return True
    else:
        return False

result = is_even(5)
print(result)

#Ejercicio 4
def convert_to_uppercase(text):
    return text.upper()

result = convert_to_uppercase("Hola")
print(result)

#Ejercicio 5
def arbitrary_sum(*args):
    total = 0
    for num in args:
        total += num
    return total

result = arbitrary_sum(1, 2, 3, 4, 5)
print(result)

#Ejercicio 6
def generate_full_greeting(name, surname):
    return f"Hola, {name} {surname}"

result = generate_full_greeting(name = "Juan", surname = "Pérez")
print(result)

#Ejercicio 7
def power(base, exponent):
    return base ** exponent

result = power(base = 2, exponent = 3)
print(result)

#Ejercicio 8
def calculate_average(num1, num2, num3):
    return (num1 + num2 + num3) / 3

result = calculate_average(1, 2, 3)
print(result)

#Ejercicio 9
def count_characters(text):
    return len(text)

result = count_characters("Hola")
print(result)

#Ejercicio 10
def display_messages(*messages):
    for message in messages:
        print(message)

display_messages("Mensaje 1", "Mensaje 2", "Mensaje 3")


