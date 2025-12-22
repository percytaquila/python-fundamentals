### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.65, "Percy", "Taquila", "Percy")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError

print(my_tuple.count("Percy"))
print(my_tuple.index("Taquila"))
print(my_tuple.index("Percy"))

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple) 

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))


my_tuple[4] = "Argentina"
my_tuple.insert(1, "Rojo")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

#del my_tuple[2]