N, M = map(int, input().split())
height = list(map(int, input().split()))


def calculate(h):
    return sum([h_ - h if h_ - h > 0 else 0 for h_ in height])


left, right = 0, max(height)
while left + 1 < right:
    mid = (left + right) // 2
    acc = calculate(mid)

    if acc >= M:
        left = mid
    elif acc < M:
        right = mid

print(left)
