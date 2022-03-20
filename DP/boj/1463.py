n = int(input())
dp = [0, 0, 1]

for i in range(3, n + 1):
    mn = dp[i - 1]
    if i % 2 == 0:
        mn = min(mn, dp[i // 2])
    if i % 3 == 0:
        mn = min(mn, dp[i // 3])
    dp.append(mn + 1)

print(dp[n])
