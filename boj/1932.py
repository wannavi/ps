n = int(input())

triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))

# dp[depth][length]

#        dp[0][0]
#    dp[1][0] dp[1][1]
# dp[2][0] dp[2][1] dp[2][2]

dp = [[triangle[0][0]]]

for i in range(1, n):
    row = []
    for j in range(i + 1):
        if j == 0:
            row.append(dp[i-1][0] + triangle[i][0])
        elif j == i:
            row.append(dp[i-1][i-1] + triangle[i][i])
        else:
            row.append(max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j])
    dp.append(row)

print(max(dp[n-1]))
