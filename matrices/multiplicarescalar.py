def multiplicar_por_escalar(matriz, escalar):
    # Inicializar la matriz resultado con ceros
    resultado = [[0 for _ in range(len(matriz[0]))] for _ in range(len(matriz))]

    # Multiplicar cada elemento de la matriz por el escalar
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            resultado[i][j] = matriz[i][j] * escalar

    return resultado

# Ejemplo de uso
matriz_A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
escalar = 2

matriz_resultado = multiplicar_por_escalar(matriz_A, escalar)

# Imprimir el resultado
for fila in matriz_resultado:
    print(fila)