N = int(input())


def hannoi(n, a, b):
    """
    n개를 위치 a에서 b로 옮길 때 횟수 반환
    """
    if n == 1:
        print(a, b)
        return

    hannoi(n-1, a, 6-a-b)
    print(a, b)
    hannoi(n-1, 6-a-b, b)


print((1 << N) - 1)
hannoi(N, 1, 3)
