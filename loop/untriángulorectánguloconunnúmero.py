#####Escriba un programa para mostrar el patrón como un triángulo rectángulo con un número.
#El patrón como:
#1
#12
#123
#1234

for e in range(4):
    for q in range (e+1):
        print(q+1, end ="")
    print("")