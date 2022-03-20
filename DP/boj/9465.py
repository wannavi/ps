"""
dp[c][stat]: c열을 stat으로 만들 때 c열까지의 최대합
"""

T = int(input())

for _ in range(T):
    n = int(input())

    mp = [list(map(int, input().split())) for _ in range(2)]
    dp = [[-1] * 3 for _ in range(n)]
    dp[0] = [0, mp[0][0], mp[1][0]]

    for i in range(1, n):
        dp[i][0] = max(dp[i - 1])
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + mp[0][i]
        dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + mp[1][i]

    print(max(dp[n - 1]))
