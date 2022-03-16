from collections import deque


n = int(input())
grid = [list(input()) for _ in range(n)]
discovered = [[False] * n for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    discovered[x][y] = True
    color = grid[x][y]

    while queue:
        curr = queue.popleft()
        for dir in range(4):
            nx, ny = curr[0] + dx[dir], curr[1] + dy[dir]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if grid[nx][ny] != color or discovered[nx][ny]:
                continue
            queue.append((nx, ny))
            discovered[nx][ny] = True


def area(n):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not discovered[i][j]:
                cnt += 1
                bfs(i, j)

    return cnt


normal = area(n)

# 방문배열 초기화
discovered = [[False] * n for _ in range(n)]
# Change all G to R
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'G':
            grid[i][j] = 'R'

abnormal = area(n)

print(normal, abnormal)
