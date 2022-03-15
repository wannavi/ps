from collections import deque


def main():
    R, C = map(int, input().split())
    grid = [list(input()) for _ in range(R)]

    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    queue = deque()
    dist = [[-1] * C for _ in range(R)]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'F':
                queue.append((i, j, 'F'))

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'J':
                queue.append((i, j, 'J'))
                dist[i][j] = 0

    while queue:
        x, y, cs = queue.popleft()
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if nx < 0 or nx >= len(grid) or \
                    ny < 0 or ny >= len(grid[0]):
                continue

            if cs == 'F' and (grid[nx][ny] == 'J' or grid[nx][ny] == '.'):
                grid[nx][ny] = 'F'
                queue.append((nx, ny, cs))

            elif cs == 'J' and (grid[nx][ny] == '.'):
                grid[nx][ny] = 'J'
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny, cs))

    possibles = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i == 0 or i == R - 1 or j == 0 or j == C - 1) and dist[i][j] != -1:
                possibles.append(dist[i][j])

    print(min(possibles) + 1 if possibles else 'IMPOSSIBLE')


if __name__ == '__main__':
    main()
