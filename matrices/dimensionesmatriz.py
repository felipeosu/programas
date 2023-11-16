def dimensiones_matriz(matriz):
    if not matriz or not matriz[0]:
        return 0, 0  

    filas = len(matriz)
    columnas = len(matriz[0])

    return filas, columnas

matriz_ejemplo = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
filas, columnas = dimensiones_matriz(matriz_ejemplo)

print("Número de filas:", filas)
print("Número de columnas:", columnas)
