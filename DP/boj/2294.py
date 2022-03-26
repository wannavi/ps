import collections


# 동전이 배수 관계가 아닐 수 있다는 점에 주목
n, k = map(int, input().split())
dp = collections.defaultdict(int)
coins = []

for _ in range(n):
    p = int(input())
    coins.append(p)
    dp[p] = 1


for i in range(1, k + 1):
    if i not in dp:
        continue

    for nxt in coins:
        if dp[i + nxt] != 0:
            dp[i + nxt] = min(dp[i + nxt], dp[i] + 1)
        else:
            dp[i + nxt] = dp[i] + 1

print(dp[k] if dp[k] else -1)
