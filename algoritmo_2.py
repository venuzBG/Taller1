# Resolucion del algoritmo de ordenamiento burbuja (Bubble Sort)
# def bubble_sort(a, inter=0):
#     n = len(a)
#     for i in range(n):
#         swapped = False
#         for j in range(1, n - i):
#             inter += 1  
#             if a[j] < a[j - 1]:
#                 a[j], a[j - 1] = a[j - 1], a[j]
#                 swapped = True
#         if not swapped:
#             break
#     return a

# length = int(input("Ingrese la longitud de la lista: "))

# Solicita los elementos uno por uno
# arr = []
# for i in range(length):
#     num = int(input(f"Ingrese el elemento {i+1}: "))
#     arr.append(num)

# print("Lista original:", arr)
# print("Lista ordenada:", bubble_sort(arr))

# V2
# arr = [-1, 0, 4, 5, 6, 7]
# print(bubble_sort(arr))  
# Algoritmo 02 - Bubble Sort (contando comparaciones)

lista = [5, 4, 3, 2, 1]
comparaciones = 0

n = len(lista)
for i in range(n - 1):
    for j in range(n - i - 1):
        comparaciones += 1  
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]  # Intercambio

print("Lista ordenada:", lista)
print("Número de comparaciones:", comparaciones)

