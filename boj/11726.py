n = int(input())


# =  : dp[0][i] = dp[0][i-2] + dp[1][i-2]
# |  : dp[1][i] = dp[0][i-1] + dp[1][i-1]

dp = [[0] * (n + 1) for _ in range(2)]
dp[0][1],  dp[1][1] = 0, 1
dp[0][2] = dp[1][2] = 1

for i in range(3, n + 1):
    dp[0][i] = (dp[0][i-2] + dp[1][i-2]) % 10007
    dp[1][i] = (dp[0][i-1] + dp[1][i-1]) % 10007

print((dp[0][n] + dp[1][n]) % 10007)
