def solution(n):
    count = one_count_in_binary(n)

    next = n + 1
    while True:
        if count == one_count_in_binary(next):
            return next

        next += 1


def one_count_in_binary(n):
    count = 0
    while n > 0:
        n, r = divmod(n, 2)
        if r == 1:
            count += 1

    return count


print(solution(78))
