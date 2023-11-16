numeros = [10, 5, 8, 20, 15, 7]


mayor = numeros[0]


for numero in numeros:
    if numero > mayor:
        mayor = numero


print("El número mayor es:", mayor)