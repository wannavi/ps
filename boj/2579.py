n = int(input())
scores = [0]

for _ in range(n):
    scores.append(int(input()))

# dp[2][n]
# 전에 1칸 이동: dp[0][k] = max(dp[0][k-1], dp[1][k-2]) + scores[k]
# 전에 2칸 이동: dp[1][k] = max(dp[0][k-2], dp[1][k-2]) + scores[k]
dp = [[0] * (n + 1) for _ in range(2)]
dp[0][1] = dp[1][1] = scores[1]

for i in range(2, n + 1):
    dp[0][i] = dp[1][i - 1] + scores[i]
    dp[1][i] = max(dp[0][i - 2], dp[1][i - 2]) + scores[i]

print(max(dp[0][n], dp[1][n]))
