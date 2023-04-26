from calculadora import area_cuadrado,area_circulo,area_triangulo
from interfaz import menu,datos_cuadrado,datos_circulo,datos_triangulo,mostrar_circulo,mostrar_cuadrado,mostrar_triangulo

"""mostrar_cuadrado(2)
mostrar_circulo(4)
mostrar_triangulo(9)"""

CUADRADO = 1
CIRCULO = 2
TRIANGULO = 3
SALIR = 4

opcion=0

while opcion != SALIR:

    opcion=menu()

    if opcion == CUADRADO:
    
     lado = datos_cuadrado()

     area=area_cuadrado(lado)

     mostrar_cuadrado(area)

    if opcion == CIRCULO:
    
     radio = datos_circulo()

     area=area_circulo(radio)

     mostrar_circulo(area)

    if opcion == TRIANGULO:
    
     base,altura = datos_triangulo()

     area=area_triangulo(base, altura)

     mostrar_triangulo(area)

    elif opcion==SALIR:
     print("Gracias por utilizar nuestra calculadora")
      
    else:
     print("opcion erronea")


      
    


