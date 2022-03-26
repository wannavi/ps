n, k = map(int, input().split())
coins = []

for _ in range(n):
    coins.append(int(input()))

# k 만드는데 필요한 최소 동전 개수
# f(k) = 1 + min(f(k - c1), f(k - c2), ... )
MAX = 1e9
dp = [0] + [MAX] * k

for i in range(1, k+1):
    res = MAX
    for coin in coins:
        if i - coin >= 0:
            res = min(res, dp[i - coin])

    dp[i] = 1 + res if res != MAX else dp[i]

print(dp[k] if dp[k] != MAX else -1)
