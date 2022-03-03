from itertools import permutations


def solution(numbers):
    return len([n for n in make_possible(numbers) if is_prime(n)])


def make_possible(numbers):
    res = []
    for i in range(1, len(numbers) + 1):
        res += list(set(permutations(numbers, len(numbers))))
    print(res)
    return [int(r) for r in res]


def is_prime(num):
    for i in range(1, int(num/2) + 1):
        if num % i == 0:
            return False

    return True


print(solution("011"))
