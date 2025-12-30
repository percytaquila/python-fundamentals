#Ejercicio 1
number = 10
if number > 0:
    print("El número es positivo")
elif number < 0:
    print("El número es negativo")
else:
    print("El número es cero")

#Ejercicio 2
age_user = input("Ingresa tu edad: ")
age = int(age_user)
if age >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#Ejercicio 3
my_text = ""
if not my_text:
    print("Mi cadena de texto es vacia")

#Ejercicio 4
number1 = input("Ingrese el valor 1: ")
number2 = input("Ingrese el valor 2: ")
number1 = int(number1)
number2 = int(number2)
if number1 > number2:
    print("El número 1 es mayor")
elif number2 > number1:
    print("El número 2 es mayor")
else:
    print("Los números son iguales")

#Ejercicio 5
number = input("Ingrese un número: ")
number = int(number)
if number % 3 == 0 and number % 5 == 0:
    print("El número es divisible por 3 y 5")
else:
    print("El número no es divisible por 3 y 5")

#Ejercicio 6
number = input("Ingrese un numero: ")
number = int(number)
if number % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

#Ejercicio 7
age_user = input("Ingresa tu edad: ")
age = int(age_user)
if age >= 18:
    print("Puedes votar")
elif age == 16 or age == 17:
    print("Puedes votar con permiso especial")
else:
    print("No puedes votar")
    
#Ejercicio 8
password_default = "123456"
password_user = input("Ingresa tu contraseña: ")
if password_user == password_default:
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")

#Ejercicio 9
number = input("Ingrese un número: ")
number = int(number)
if number >= 10 and number <= 20:
    print("El número está entre 10 y 20")
else:
    print("El número no está entre 10 y 20")

#Ejercicio 10
semaforo = input("Ingrese un color de semáforo: ")
if semaforo == "rojo":
    print("Detenerse")
elif semaforo == "amarillo":
    print("Precaucion")
elif semaforo == "verde":
    print("Continuar")
else:
    print("Color de semáforo no reconocido")