t = int(input())

for _ in range(t):
    n = int(input())
    arr = []
    for _ in range(2):
        arr.append(list(map(int, input().split())))

    # dp[n][3]
    dp = [[0, 0, 0] for _ in range(n)]
    dp[0] = [0, arr[0][0], arr[1][0]]

    for i in range(1, n):
        dp[i][0] = max(dp[i-1][1], dp[i-1][2])
        dp[i][1] = arr[0][i] + max(dp[i-1][0], dp[i-1][2])
        dp[i][2] = arr[1][i] + max(dp[i-1][0], dp[i-1][1])

    print(max(dp[n-1]))
