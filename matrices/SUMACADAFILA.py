def suma_filas_columnas(matriz):
    # Verificar si la matriz es vacía
    if not matriz or not matriz[0]:
        return "La matriz está vacía."

    # Inicializar listas para almacenar las sumas de filas y columnas
    sumas_filas = [sum(fila) for fila in matriz]
    sumas_columnas = [sum(columna) for columna in zip(*matriz)]

    return sumas_filas, sumas_columnas

# Ejemplo de uso
matriz_ejemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

sumas_filas, sumas_columnas = suma_filas_columnas(matriz_ejemplo)

print("Sumas de filas:", sumas_filas)
print("Sumas de columnas:", sumas_columnas)

