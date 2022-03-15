from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# BFS
def solution(maps):
    queue = deque([(0, 0)])  # y, x

    while queue:
        y, x = queue.popleft()
        for dir in range(4):
            ny, nx = y + dy[dir], x + dx[dir]

            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and maps[ny][nx] == 1:
                maps[ny][nx] = maps[y][x] + 1
                queue.append((ny, nx))

    return maps[-1][-1]


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
    1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
