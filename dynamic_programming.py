def fibonacci(n):
    if n <= 1:
        return n
    # inisialisai tabel
    fib = [0] * (n + 1)
    fib[1] = 1

    # mengisi tabel
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]

print(fibonacci(10))