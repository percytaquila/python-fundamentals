### Classes ###

""" class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson) """

class Person:
    def __init__(self, name, surname, alis = "Sin alias"):
        self.full_name = f"{name} {surname} ({alis})"
        self.__name = name # Propiedad privada
        self.__surname = surname

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def walk(self):
        print(f"{self.full_name} está caminando")

my_person = Person("Percy", "Taquila")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Percy", "Taquila", "ClownN")
print(my_other_person.full_name)
my_other_person.walk()