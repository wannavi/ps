from collections import deque


m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

# Find all 1 and append to queue
queue = deque()
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 1:
            queue.append((i, j))

while queue:
    x, y = queue.popleft()
    for dir in range(4):
        nx, ny = x + dx[dir], y + dy[dir]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if grid[nx][ny] != 0:
            continue
        queue.append((nx, ny))
        grid[nx][ny] = grid[x][y] + 1


mx = 0
flag = False
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 0:
            print(-1)
            flag = True
        else:
            mx = max(mx, grid[i][j])
    if flag:
        break

print(mx - 1)
