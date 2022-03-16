# n 은 3의 거듭제곱 꼴
n = int(input())
grid = [['*'] * n for _ in range(n)]


def solve(n: int, x: int, y: int):
    # 재귀적으로 가운데 구멍 뚫는 함수
    if n == 1:
        return

    # 가운데 구멍 뚫기
    for i in range(x + n//3, x + 2 * n//3):
        for j in range(y + n//3, y + 2 * n//3):
            grid[i][j] = ' '

    # 사이드 8개
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            solve(n//3, x + n//3 * i, y + n//3 * j)


solve(n, 0, 0)

for row in grid:
    print(''.join(row))
