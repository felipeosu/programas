numeros = [10, 5, 8, 20, 15, 7]


suma = 0

cantidad = 0

for numero in numeros:
    suma += numero
    cantidad += 1

if cantidad > 0:
    media = suma / cantidad
    print("La media es:", media)
