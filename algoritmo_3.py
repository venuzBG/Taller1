# Resolucion del algoritmo de la sucesion de Fibonacci
# def Fibonacci(n):
#     if n == 0:
#         return 0
#     else:
#         x = 0
#         y = 1
#         for i in range(1, n):
#             z = x + y
#             x = y
#             y = z
#         return y

# n = int(input("Ingrese el valor de n: "))
# resultado = Fibonacci(n)
# print(f"Para n = {n}, y = {resultado}")

import math

# Valor real del número áureo
phi = (1 + math.sqrt(5)) / 2

# Generar términos de Fibonacci con redondeo a 3 cifras
fib = [1.00, 1.00]

# Redondear a 3 cifras significativas
def redondear(x):
    return float(f"{x:.3g}")

# Crear secuencia con redondeo
for i in range(2, 20):
    nuevo = redondear(fib[-1] + fib[-2])
    fib.append(nuevo)

# Calcular las razones y su error relativo
for i in range(1, len(fib) - 1):
    r = redondear(fib[i + 1] / fib[i])
    error_relativo = abs((r - phi) / phi)
    print(f"i={i:2d}  y_i={fib[i]:7.3f}  r={r:6.3f}  error={error_relativo:.2e}")
    if error_relativo < 1e-5:
        print(f"\n Desde la iteración i={i}, el error relativo es menor que 1e-5")
        break