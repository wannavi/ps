from collections import deque


def main():
    M, N, H = map(int, input().split())
    grid, dist = [], []
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    for _ in range(H):
        grid.append(
            [list(map(int, input().split())) for _ in range(N)]
        )
        dist.append([[-1]*M for _ in range(N)])

    queue = deque()

    # 익은 토마토 찾기
    for z in range(H):
        for x in range(N):
            for y in range(M):
                if grid[z][x][y] == 1:
                    queue.append((z, x, y))
                    dist[z][x][y] = 0

    while queue:
        z, x, y = queue.popleft()
        for dir in range(6):
            nz, nx, ny = z + dz[dir], x + dx[dir], y + dy[dir]
            if 0 > nz or nz >= H or 0 > nx or nx >= N or \
                    0 > ny or ny >= M:
                continue
            if grid[nz][nx][ny] != 0 or dist[nz][nx][ny] != -1:
                continue

            queue.append((nz, nx, ny))
            dist[nz][nx][ny] = dist[z][x][y] + 1

    mx = -1
    for z in range(H):
        for x in range(N):
            for y in range(M):
                if dist[z][x][y] == -1 and grid[z][x][y] != -1:
                    print(-1)
                    return
                mx = max(mx, dist[z][x][y])

    print(mx)


if __name__ == '__main__':
    main()
