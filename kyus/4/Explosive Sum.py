def exp_sum(n):
    if n <= 3:
        return n
    
    memo = [1] + [0] * n
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            memo[j] += memo[j - i]
    return memo[-1]
