import collections


import collections

N = int(input())
dp = collections.defaultdict(int)


def fibo(n):
    if n <= 1:
        return n

    if dp[n]:
        return dp[n]

    dp[n] = fibo(n - 1) + fibo(n - 2)
    return dp[n]


print(N, fibo(N))
