# Ejercicio 1
import calculator

calculator.sumar(1, 2)
calculator.restar(1, 2)
calculator.multiplicar(1, 2)
calculator.dividir(1, 2)


# Ejercicio 2
import converter

converter.convert_celsius(10)
converter.convert_fahrenheit(10)


# Ejercicio 3
import lista_estudiantes
lista_estudiantes.ver_estudiantes()

# Ejercicio 4
import geometry

print(geometry.area_cuadrado(10))
print(geometry.area_circulo(10))


# Ejercicio 5
from sum_module import sum_all
print(sum_all(1, 2, 3, 4, 5))


# Ejercicio 6
from car_module import Car
my_car = Car("Toyota", "Corolla", 2022)
print(my_car.display_info())

# Ejercicio 7
from file_module import write_to_file, read_from_file
write_to_file("example.txt", "Hola, Python")
print(read_from_file("example.txt"))

# Ejercicio 8

from statistics import mean, median
numbers = [1, 2, 3, 4, 5]
print(mean(numbers))
print(median(numbers))

# Ejercicio 9
from word_count import count_word
text = "Python is great and Python is fun"
print(count_word(text, "python"))


# Ejercicio 10
from dates import fecha_actual, diferencia_fechas
print(fecha_actual())
print(diferencia_fechas("01-01-2025", "01-10-2025"))