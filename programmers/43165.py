# https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    count = 0

    def dfs(index, sum):
        nonlocal count
        if index == len(numbers):
            if sum == target:
                count += 1
        else:
            dfs(index+1, sum+numbers[index])
            dfs(index+1, sum-numbers[index])

    dfs(0, 0)
    return count


def solution(numbers, target):
    count = 0

    stack = [(0, 0)]  # (localSum, index)
    while stack:
        localSum, index = stack.pop()

        if index == len(numbers):
            if localSum == target:
                count += 1
        else:
            n = numbers[index]
            stack.append((localSum + n, index + 1))
            stack.append((localSum - n, index + 1))

    return count
