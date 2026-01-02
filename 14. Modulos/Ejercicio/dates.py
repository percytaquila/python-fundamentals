from datetime import datetime

def fecha_actual():
    return datetime.now().strftime("%d-%m-%Y")

def diferencia_fechas(fecha1, fecha2):
    d1 = datetime.strptime(fecha1, "%d-%m-%Y")
    d2 = datetime.strptime(fecha2, "%d-%m-%Y")
    return abs((d2 - d1).days)

