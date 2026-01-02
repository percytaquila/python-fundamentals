### Excpetion Handling ###

numberOne = 5
numberTwo = 1
numberTwo = "1"


# try excep else finally

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else: # Opcional
    # Se ejecuta si no se produce una excepción
    print("La ejecución continua correctamente")
finally: # Opciona
    # Se ejecuta siempre
    print("La ejecución continua")


# Expceptiones por tipo

try: 
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")

# Captura de la información de la excepción

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except TypeError as error:
    print(error)
except Exception as error:
    print(error)