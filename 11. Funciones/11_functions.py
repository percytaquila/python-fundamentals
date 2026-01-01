### Functions ###

def my_function():
    print("Esto es una función")

my_function()
my_function()
my_function()


def sum_two_values (first_number: int, second_number: int):
    print(first_number + second_number)

sum_two_values(5, 7)
sum_two_values("5", "7")
sum_two_values(1.4, 5.2)



def sum_two_values_with_return (first_number, second_number):
    my_sum = first_number + second_number
    return my_sum

my_result = sum_two_values_with_return(10, 5)
print(my_result)

def print_name (name, surname):
    print(f"{name} {surname}")

print_name(surname="Taquila", name="Percy")

def print_name_with_default (name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Percy", "Taquila", "ClownN")
print_name_with_default("Percy", "Taquila")

def print_text(*text):
    print(text)

print_text("Hola", "Python", "Percy")
print_text("Hola")

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())

print_upper_texts("Hola", "Python", "Percy")
print_upper_texts("Hola")