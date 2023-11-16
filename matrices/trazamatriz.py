def traza_matriz(matriz):
    if len(matriz) != len(matriz[0]):
        raise ValueError("La matriz debe ser cuadrada para calcular la traza.")

    traza = sum(matriz[i][i] for i in range(len(matriz)))

    return traza

matriz_ejemplo = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

traza = traza_matriz(matriz_ejemplo)

print("La traza de la matriz es:", traza)
