# Resolucion del algoritmo de la sucesion de Fibonacci
def Fibonacci(n):
    if n == 0:
        return 0
    else:
        x = 0
        y = 1
        for i in range(1, n):
            z = x + y
            x = y
            y = z
        return y

n = int(input("Ingrese el valor de n: "))
resultado = Fibonacci(n)
print(f"Para n = {n}, y = {resultado}")