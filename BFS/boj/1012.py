from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def bfs(grid, x, y):
    queue = deque()
    queue.append((x, y))
    grid[x][y] = 0

    while queue:
        curr = queue.popleft()
        for dir in range(4):
            nx, ny = curr[0] + dx[dir], curr[1] + dy[dir]
            if 0 > nx or nx >= len(grid) or \
                    0 > ny or ny >= len(grid[0]):
                continue
            if grid[nx][ny] != 1:
                continue
            queue.append((nx, ny))
            grid[nx][ny] = 0


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    grid = [[0]*m for _ in range(n)]

    for _ in range(k):
        y, x = map(int, input().split())
        grid[x][y] = 1

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                bfs(grid, i, j)
                count += 1

    print(count)
