def menu():
    print("calculadora de figuras geometricas")
    print("1. calcular area del cuadrado")
    print("2. calcular area del circulo")
    print("3. calcular area del triangulo")
    print("4.salir")
    op = int(input("digite su opcion: "))
    return op


def datos_cuadrado():

    "solicitar el lado del cuadrado y lo transforma y lo retorna float"
    
    lado=float(input("digite el lado"))
    return lado

def datos_circulo(): 

    "solicitar el radio del circulo y lo transforma y lo retorna float"
    
    radio=float(input("digite el radio: "))
    return radio

def datos_triangulo():

    "solicitar el base y altura  del triangulo y lo transforma y lo retorna float"
    
    base = float(input("digite la base: "))
    altura = float(input("digite la altura: "))
    return base, altura

def mostrar_cuadrado(area):

    """mostrar el area de cuadrado"""

    print(f"el area del cuadrado es {area} mts")


def mostrar_circulo(area):

    """mostrar el area de circulo"""

    print(f"el area del circulo es {area} mts")

def mostrar_triangulo(area):

    """mostrar el area de cuadrado"""

    print(f"el area del triangulo es {area} mts")
