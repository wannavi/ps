# 메모리 초과로 풀이 불가능

import collections
import sys

sys.setrecursionlimit(1000000)

n = int(input())
dp = collections.defaultdict(int)
dp[1], dp[2] = 0, 1


def F(n):
    if n in dp:
        return dp[n]

    mn = F(n - 1)
    if n % 2 == 0:
        mn = min(mn, F(n // 2))
    if n % 3 == 0:
        mn = min(mn, F(n // 3))

    dp[n] = mn + 1
    return dp[n]


print(F(n))
