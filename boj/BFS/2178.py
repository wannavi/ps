from collections import deque


n, m = map(int, input().split())

maps, dist = [], [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    maps.append(list(map(int, list(input()))))

queue = deque([(0, 0)])
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
dist[0][0] = 1

while queue:
    y, x = queue.popleft()
    for dir in range(4):
        ny, nx = y + dy[dir], x + dx[dir]
        if not (0 <= ny < len(maps) and 0 <= nx < len(maps[0])):
            continue
        if dist[ny][nx] != 0 or maps[ny][nx] == 0:
            continue

        dist[ny][nx] = dist[y][x] + 1
        queue.append((ny, nx))

print(dist[-1][-1])
