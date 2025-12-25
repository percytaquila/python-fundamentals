
# Ejercicio 1
my_tuple = tuple()
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple)

# Ejercicio 2
my_tuple = (100, 200, 300, 400, 500)
print(my_tuple[1])

# Ejercicio 3
""" my_tuple_2 = tuple()
my_tuple_2 = (1, 2, 3)
my_tuple[0] = 10 """

# Ejercicio 4
my_tuple_3 = tuple()
my_tuple_3 = (1, 2, 3, 3, 4, 5, 3)
print(my_tuple_3.count(3))

# Ejercicio 5
my_tuple_4 = tuple()
my_tuple_4 = ("Java", "Python", "JavaScript", "Python")
print(my_tuple_4.index("Python"))

# Ejercicio 6
my_tuple_5 = tuple()
my_tuple_6 = tuple()

my_tuple_5 = (1, 2, 3)
my_tuple_6 = (4, 5, 6)

my_tuple_7 = my_tuple_5 + my_tuple_6
print(my_tuple_7)

# Ejercicio 7
my_tuple = (10, 20, 30, 40, 50)
my_subtuple = my_tuple[2:4]
print(my_subtuple)

# Ejercicio 8
my_tuple_test = tuple()
my_tuple_test = ("rojo", "verde", "azul")
my_tuple_test = list(my_tuple_test)
my_tuple_test[1] = "amarillo"
my_tuple_test = tuple(my_tuple_test)
print(my_tuple_test)

# Ejercicio 9
my_tuple = (1, 2, 3)
del my_tuple

# Ejercicio 10
my_tuple = (100, )
print(my_tuple)
