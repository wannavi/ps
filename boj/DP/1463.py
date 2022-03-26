n = int(input())

dp = {1: 0, 2: 1}
for i in range(3, n + 1):
    cand = dp[i-1]
    if i % 3 == 0:
        cand = min(dp[i//3], cand)
    if i % 2 == 0:
        cand = min(dp[i//2], cand)
    dp[i] = cand + 1

print(dp[n])
