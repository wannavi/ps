m, n = 10, 7    # 세로, 가로
grid = []
discovered = [[False]*n for _ in range(m)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

# DFS
stack = []
order = []  # 정점 방문 순서
stack.append((0, 0))
discovered[0][0] = True

while stack:
    x, y = stack.pop()
    order.append((x, y))
    for dir in range(4):
        nx, ny = x + dx[dir], y + dy[dir]
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        if discovered[nx][ny] and grid[nx][ny] != 1:
            continue

        stack.append((nx, ny))
        discovered[nx][ny] = True
