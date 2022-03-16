ret = 1
A, B, C = map(int, input().split())


def pow(a, b, m):
    """
    a^2n % m = (a^n % m) ^ 2
    a^(2n+1) % m = (a^n % m) ^ 2 * (a % m)
    """
    if b == 1:
        return a % m
    val = pow(a, b//2, m)
    val = val * val % m
    if b % 2 == 0:
        return val
    return val * a % m


print(pow(A, B, C))
