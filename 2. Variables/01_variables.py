# Variables

my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = 5
print(my_string_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)                            

# Concatenación de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable)
print("Este es el valor de: ", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola línea.
name, surname, alias, age = "Percy", "Taquila", "ptaquila", 29
print("Me llamo:", name, surname, ". Mi edad es:", age, ". Y mi alias es:", alias)

# Inputs

""" 
    first_name = input("cual es tu nombre? ")
    age = input("cual es tu edad? ")

    print(first_name)
    print(age) 
"""

# Cambiamos su tipo
name = 29
age = "Percy"
print(name)
print(age)

# Formzamos el tipo
address: str = "Mi dirección"
address = 32
print(address)
print(type(address))