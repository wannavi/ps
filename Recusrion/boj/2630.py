n = int(input())
grid = [list(map(int, input().split()))
        for _ in range(n)]


def check(n: int, x: int, y: int, c: int) -> bool:
    # 해당 영역이 전부 c로 칠해져있는지 여부 반환
    for i in range(x, x + n):
        for j in range(y, y + n):
            if grid[i][j] != c:
                return False

    return True


def count(n: int, x: int, y: int, c: int) -> int:
    # 해당 영역, c 색깔 색종이 카운트
    if check(n, x, y, c):
        return 1
    elif n == 1 and not check(n, x, y, c):
        return 0

    # 4개 구역으로 쪼개서 더하기
    ans = count(n//2, x, y, c) + \
        count(n//2, x + n//2, y, c) + \
        count(n//2, x, y + n//2, c) + \
        count(n//2, x + n//2, y + n//2, c)

    return ans


print(count(n, 0, 0, 0))
print(count(n, 0, 0, 1))
