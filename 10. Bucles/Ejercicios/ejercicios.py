#Ejercicio 1

indice = 1

while indice <= 10:    
    print(indice)
    indice += 1

#Ejercicio 2
my_list = [10, 20, 30, 40, 50]

for element in my_list:
    print(element)

#Ejercicio 3

indice = 1
resultado = 0

while indice <= 100:
    resultado += indice
    indice += 1

print(resultado)

#Ejercicio 4
text = "Python"

for letter in text:
    print(letter)

#Ejercicio 5
indice = 1
while indice <= 50:
    if(indice % 7 == 0):
        print(indice)
        break
    indice += 1

#Ejercicio 6
my_dict = {"name": "Brais", "age": 37, "country": "Galicia"}

for element in my_dict:
    print(element)


#Ejercicio 7
indice = 1

while indice <= 20:
    if(indice % 2 == 0):
        print(indice)
    indice += 1

#Ejercicio 8

for i in range(10, 0, -1):
    print(i)

#Ejercicio 9
my_list = [30, 10, 30, 20, 30, 40]
repetidos = 0

for element in my_list:
    if element == 30:
        repetidos += 1

print(repetidos)

#Ejercicio 10
my_list = ["Percy", "Oscar", "Brais", "Jose", "Andrea", "Maria"]

for element in my_list:
    if element == "Brais":
        break
    print(element)