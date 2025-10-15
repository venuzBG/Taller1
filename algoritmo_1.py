# Ejercicio de error absoluto

# Suma la serie 1 + 1/2 + 1/4 + ... hasta que el error absoluto sea menor que 10^1

suma = 0
termino = 1
n = 0
while abs(termino) >= 10**-1:
    suma += termino
    n += 1
    termino = 1 / (2 ** (n+1))
    n += 1

print("La suma de la serie es:", suma)
print("El número de términos sumados es:", n)
# Resolucion del algoritmo de ordenamiento burbuja (Bubble Sort)
