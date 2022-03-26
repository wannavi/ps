from sys import stdin
from collections import deque
input = stdin.readline


n = int(input())
grid = [list(map(int, input())) for _ in range(n)]


def DFS(i, j):
    if i < 0 or i >= len(grid) or \
            j < 0 or j >= len(grid[0]) or \
            grid[i][j] == 0:
        return 0

    grid[i][j] = 0

    count = 1 + DFS(i + 1, j) + \
        DFS(i - 1, j) + \
        DFS(i, j + 1) + \
        DFS(i, j - 1)

    return count


results, count = [], 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 1:
            results.append(DFS(i, j))
            count += 1

results.sort()

print(count)
for result in results:
    print(result)
