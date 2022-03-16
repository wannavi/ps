from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, list(input()))) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

# BFS - 최단 경로
queue = deque([(0, 0)])
dist[0][0] = 0

while queue:
    x, y = queue.popleft()
    for dir in range(4):
        nx, ny = x + dx[dir], y + dy[dir]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if grid[nx][ny] != 1 or dist[nx][ny] != -1:
            continue

        queue.append((nx, ny))
        dist[nx][ny] = dist[x][y] + 1

print(dist[-1][-1] + 1)
