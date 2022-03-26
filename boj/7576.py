from collections import deque


m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def BFS():
    queue = deque([])

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]

            if nx < 0 or nx >= len(grid) or \
                    ny < 0 or ny >= len(grid[0]) or \
                    grid[nx][ny] != 0:
                continue

            grid[nx][ny] = grid[x][y] + 1
            queue.append((nx, ny))


BFS()


def solution():
    mx = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                print(-1)
                return
            else:
                mx = max(mx, grid[i][j])

    print(mx - 1)


solution()
