def multiplicar_matrices(matriz1, matriz2):
    if len(matriz1[0]) != len(matriz2):
        raise ValueError("El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz para poder multiplicarlas.")

    resultado = [[0 for _ in range(len(matriz2[0]))] for _ in range(len(matriz1))]

    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            for k in range(len(matriz2)):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]

    return resultado

matriz_A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz_B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

matriz_resultado = multiplicar_matrices(matriz_A, matriz_B)

for fila in matriz_resultado:
    print(fila)