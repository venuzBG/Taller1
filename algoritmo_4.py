import matplotlib.pyplot as plt

# Generar la serie de Fibonacci
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

# Cantidad de términos
n = 40
fib = fibonacci(n)

razones = [fib[i] / fib[i - 1] for i in range(2, len(fib))]

indices = list(range(2, len(fib)))

phi = (1 + 5 ** 0.5) / 2

# Graficar las razones y el número áureo
plt.figure()
plt.plot(indices, razones, marker='o', label='fib(n)/fib(n-1)')
plt.axhline(y=phi, color='r', linestyle='--', label='Número áureo (φ)')
plt.title('Aproximación al número áureo con la serie de Fibonacci')
plt.xlabel('n')
plt.ylabel('fib(n) / fib(n-1)')
plt.legend()
plt.grid(True)
plt.show()