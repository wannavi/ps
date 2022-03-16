from collections import deque


r, c = map(int, input().split())
grid = [list(input()) for _ in range(r)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

queue = deque()
dist = [[0]*c for _ in range(r)]

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'F':
            queue.append((i, j, 'F'))

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'J':
            queue.append((i, j, 'J'))
            dist[i][j] = 1

while queue:
    x, y, role = queue.popleft()
    for dir in range(4):
        nx, ny = x + dx[dir], y + dy[dir]
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue

        if role == 'F' and (grid[nx][ny] == 'J' or grid[nx][ny] == '.'):
            grid[nx][ny] = 'F'
            queue.append((nx, ny, 'F'))
        elif role == 'J' and (grid[nx][ny] == '.'):
            grid[nx][ny] = 'J'
            dist[nx][ny] = dist[x][y] + 1
            queue.append((nx, ny, 'J'))

ends = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (i == 0 or i == r - 1 or j == 0 or j == c - 1) and dist[i][j] != 0:
            ends.append(dist[i][j])


print(min(ends) if ends else 'IMPOSSIBLE')
