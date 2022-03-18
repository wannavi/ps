from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.bfs(i, j, grid)
                    count += 1

        return count

    def bfs(self, i: int, j: int, grid: List[List[str]]):
        queue = deque()
        queue.append((i, j))

        while queue:
            x, y = queue.popleft()
            for dir in range(4):
                nx, ny = x + dx[dir], y + dy[dir]
                if nx < 0 or nx >= len(grid) or \
                        ny < 0 or ny >= len(grid[0]):
                    continue
                if grid[nx][ny] == '0':
                    continue

                grid[nx][ny] = '0'
                queue.append((nx, ny))
