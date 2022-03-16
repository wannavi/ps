from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def bfs(x, y):
    queue = deque([(x, y)])
    grid[x][y] = 0
    area = 1
    while queue:
        v = queue.popleft()
        for dir in range(4):
            nx, ny = v[0] + dx[dir], v[1] + dy[dir]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if grid[nx][ny] != 1:
                continue
            grid[nx][ny] = 0
            area += 1
            queue.append((nx, ny))

    return area


count, mx = 0, 0
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] == 1:
            mx = max(mx, bfs(x, y))
            count += 1

print(count, mx, sep='\n')
