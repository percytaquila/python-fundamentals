#Ejercicio 1
dictionary = {"name":"Percy", "age":"30", "country":"Tacna" }
print(dictionary)

#Ejercicio 2
print(dictionary["name"])

#Ejercicio 3
dictionary["job"] = "Programador"
print(dictionary)

#Ejercicio 4
dictionary["age"] = 38
print(dictionary)

#Ejercicio 5
dictionary.pop("country")
print(dictionary)

#Ejercicio 6
new_dictionary = {1:1, 2:4, 3:9, 4:16, 5:25}
print(new_dictionary)

#Ejercicio 7
dictionary = {"name": "Percy", "age": 30, "country": "Tacna"}
print("age" in dictionary)

#Ejercicio 8
print(dictionary.keys())

#Ejercicio 9
print(list(dictionary.keys()))

#Ejercicio 10
my_keys = ["name", "age", "job"]
my_new_dict = dict.fromkeys(my_keys, "Desconocido")
print(my_new_dict)

print(my_new_dict.items())
