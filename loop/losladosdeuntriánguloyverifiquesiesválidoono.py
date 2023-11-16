####Escriba un programa para ingresar todos los lados de un triángulo y verifique si es válido o no.
lado1 = float(input("Ingrese la longitud del primer lado: "))
lado2 = float(input("Ingrese la longitud del segundo lado: "))
lado3 = float(input("Ingrese la longitud del tercer lado: "))

# Verificar si los lados forman un triángulo válido
if (lado1 + lado2 >lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("Los lados ingresados forman un triángulo válido.")
else:
    print("Los lados ingresados no forman un triángulo válido.")
