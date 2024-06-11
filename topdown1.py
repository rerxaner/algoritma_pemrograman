def fibonacci_top_down(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    memo[n] = fibonacci_top_down(n - 1, memo) + fibonacci_top_down(n - 2, memo)
    return memo[n]

print(fibonacci_top_down(10))