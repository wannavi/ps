n = int(input())
rgbs = []

for _ in range(n):
    rgbs.append(list(map(int, input().split())))

# dp[3][n] = n번째까지 비용 최솟값
dp = [[0] * 3 for _ in range(n)]
dp[0] = rgbs[0]

for i in range(1, len(rgbs)):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + rgbs[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + rgbs[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + rgbs[i][2]

print(min(dp[n-1]))

