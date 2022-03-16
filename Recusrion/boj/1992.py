N = int(input())
grid = [list(map(int, list(input())))
        for _ in range(N)]


def check(n: int, x: int, y: int) -> bool:
    # 모두 같은 숫자인지 체크
    picked = grid[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if picked != grid[i][j]:
                return False

    return True


def compress(n: int, x: int, y: int) -> str:
    # ( _ ) 꼴로 반환
    if n == 1:
        return str(grid[x][y])

    if check(n, x, y):
        return str(grid[x][y])

    ans = compress(n//2, x, y) + \
        compress(n//2, x, y + n//2) + \
        compress(n//2, x + n//2, y) + \
        compress(n//2, x + n//2, y + n//2)

    return '(' + ans + ')'


print(compress(N, 0, 0))
