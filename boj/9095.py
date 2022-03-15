dp = {0: 1, 1: 1, 2: 2}

for _ in range(int(input())):
    n = int(input())

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    print(dp[n])
