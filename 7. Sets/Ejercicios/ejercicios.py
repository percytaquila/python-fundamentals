#Ejercicio 1
my_set = {1, 2, 3, 4, 5}
print(my_set)

#Ejercicio 2
my_set.add(6)
print(my_set)

#Ejercicio 3
my_set.add(5)
print(my_set)

#Ejercicio 4
print(3 in my_set)

#Ejercicio 5
my_set.remove(4)
print(my_set)

#Ejercicio 6
my_set.clear()
print(len(my_set))

#Ejercicio 7
new_my_set = {"Manzana", "Naranja", "Platano"}
my_list = list(new_my_set)
print(my_list[0])

#Ejercicio 8
one_set = {1, 2, 3}
two_set = {4, 5, 6}
print(one_set.union(two_set))

#Ejercicio 9
my_set = {1, 2, 3, 4}
new_set = {3, 4, 5, 6}
print(my_set.difference(new_set))

#Ejercicio 10
my_set = {1, 2, 3, 4}
del my_set
print(my_set)
