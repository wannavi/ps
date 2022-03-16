N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
cnt = [0] * 3  # -1, 0, 1로 채워진 종이 갯수


def check(x: int, y: int, n: int) -> bool:
    for i in range(x, x + n):
        for j in range(y, y + n):
            if (paper[x][y] != paper[i][j]):
                return False
    return True


def solve(x: int, y: int, z: int):
    if check(x, y, z):
        cnt[paper[x][y] + 1] += 1
        return

    n = z // 3
    for i in range(3):
        for j in range(3):
            solve(x + i * n, y + j * n, n)


solve(0, 0, N)
for c in cnt:
    print(c)
