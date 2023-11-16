####Escriba un programa para verificar si un caracter está en mayúsculas o en minúscula.
caracter = input("Ingrese un carácter: ")

if caracter.isupper():
    print(f"'{caracter}' está en mayúscula.")
elif caracter.islower():
    print(f"'{caracter}' está en minúscula.")
else:
    print(f"'{caracter}' no es una letra (puede ser un numero o signos de puntuacion.)")