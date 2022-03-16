from collections import deque

dx, dy = [1, -1, 0, 0, ], [0, 0, 1, -1]

T = int(input())
for _ in range(T):
    w, h = map(int, input().split())
    grid = [list(input()) for _ in range(h)]
    dist = [[-1]*w for _ in range(h)]

    queue = deque()

    # 불 먼저 처리 -> 사람 처리
    # 최단 거리 문제임을 확인
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '*':
                queue.append((i, j, '*'))

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '@':
                queue.append((i, j, '@'))
                dist[i][j] = 1

    # BFS - 최단거리 문제
    while queue:
        x, y, role = queue.popleft()
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue

            if role == '*' and (grid[nx][ny] != '#' and grid[nx][ny] != '*'):
                queue.append((nx, ny, '*'))
                grid[nx][ny] = '*'
            elif role == '@' and (grid[nx][ny] == '.' and dist[nx][ny] == -1):
                queue.append((nx, ny, '@'))
                dist[nx][ny] = dist[x][y] + 1

    # 사이드에 도착하였는지 체크
    mn = 1e9
    for i in (0, h-1):
        for j in range(w):
            if dist[i][j] != -1:
                mn = min(mn, dist[i][j])

    for i in range(h):
        for j in (0, w-1):
            if dist[i][j] != -1:
                mn = min(mn, dist[i][j])

    print(mn if mn != 1e9 else 'IMPOSSIBLE')
