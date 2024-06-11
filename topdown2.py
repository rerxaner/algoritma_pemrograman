def knapsack_top_down(W, wt, val, n, memo = None):
    if memo is None:
        memo = {}
    if  (n, W) in memo:
        return memo[(n, W)]
    if n == 0 or W == 0:
        return 0
    if wt[n - 1] > W:
        memo[(n,W)] = knapsack_top_down(W, wt, val,n - 1, memo)
        return memo[(n, W)]
    else:
        memo[(n, W)] = max(val[n - 1] + knapsack_top_down(W - wt[n -1], wt, val, n - 1, memo), knapsack_top_down(W, wt, val, n - 1, memo))
        return memo[(n, W)]

W = 50
wt = [10, 20 ,30]
val = [60, 100, 120]
n = len(val)
print(knapsack_top_down(W, wt, val, n))