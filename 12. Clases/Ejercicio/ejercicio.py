#Ejercicio 1
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("Sonido genérico!")

#Ejercicio 2
class Animal:
    def __init__(self, species):
        self.species = species


    def make_sound(self):
        if self.species == "dog":
            print("Guau")
        elif self.species == "cat":
            print("Miau")
        else:
            print("Sonido animal genÃ©rico")

#Ejercicio 3
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.__speed = 0

#Ejercicio 4
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.__speed = 0
    
    def accelerate(self):
        self.__speed += 10

    def brake(self):
        self._speed = max(0, self._speed - 10)

#Ejercicio 5
class Book:
    def __init__(self, title, author):
        self.title = title
        self.__author = author

    def get_author(self):
        return self.__author
    
    def set_author(self, new_author):
        self.__author = new_author

#Ejercicio 6
class Estudiante:
    def __init__(self, nombre, apellido, notas):
        self.nombre = nombre
        self.apellido = apellido
        self.notas = notas

    def calcular_promedio(self):
        return sum(self.notas) / len(self.notas)

#Ejercicio 7
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Saldo insuficiente")

#Ejercicio 8
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_distance(self, other_point):
        distance_x = abs(self.x - other_point.x)
        distance_y = abs(self.y - other_point.y)
        return (distance_x ** 2 + distance_y ** 2) ** 0.5

#Ejercicio 9
class Employee:
    def __init__(self, name, hourly_wage, hours_worked):
        self.name = name
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
    
    def caculate_salary(self):
        return self.hourly_wage * self.hours_worked


#Ejercicio 10
class Store: 
    def __init__(self, inventory):
        self.inventory = inventory

    def add_product(self, product):
        self.inventory.append(product)

    def view_inventory(self):
        for product in self.inventory:
            print(product)