from collections import deque


dx = [2, 1, -1, -2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

for _ in range(int(input())):
    I = int(input())
    st, en = tuple(map(int, input().split())), tuple(map(int, input().split()))
    dist = [[-1]*I for _ in range(I)]

    queue = deque()
    queue.append(st)
    dist[st[0]][st[1]] = 0

    while dist[en[0]][en[1]] == -1:
        x, y = queue.popleft()
        for dir in range(8):
            nx, ny = x + dx[dir], y + dy[dir]
            if nx < 0 or nx >= I or ny < 0 or ny >= I:
                continue
            if dist[nx][ny] >= 0:
                continue

            queue.append((nx, ny))
            dist[nx][ny] = dist[x][y] + 1

    print(dist[en[0]][en[1]])
