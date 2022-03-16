def recursive_print(n):
    if n == 0:
        return

    print(n)
    recursive_print(n-1)


def recursive_sum(n):
    if n == 1:
        return 1

    return n + recursive_sum(n - 1)
