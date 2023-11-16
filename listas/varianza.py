numeros = [10, 5, 8, 20, 15, 7]

media = sum(numeros) / len(numeros)

suma_cuadrados_diferencias = 0
for numero in numeros:
    diferencia = numero - media
    suma_cuadrados_diferencias += diferencia ** 2

varianza = suma_cuadrados_diferencias / len(numeros)

print("La varianza es:", varianza)