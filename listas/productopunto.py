vector1 = [2, 4, 6]
vector2 = [1, 3, 5]

producto_punto = 0
for i in range(len(vector1)):
    producto_punto += vector1[i] * vector2[i]

print("El producto punto es:", producto_punto)
