###Escriba un programa que dado un número imprima la suma de sus dígitos

# Solicitar al usuario que ingrese un número
numero = int(input("Ingrese un número: "))

# Convertir el número en una cadena de caracteres
numero_str = str(numero)

# Inicializar una variable para almacenar la suma de los dígitos
suma_digitos = 0

# Iterar a través de los caracteres de la cadena e sumar cada dígito
for digito in numero_str:
    suma_digitos += int(digito)

# Mostrar la suma de los dígitos
print(f"La suma de los dígitos de {numero} es {suma_digitos}.")
