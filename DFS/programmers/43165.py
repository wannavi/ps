from typing import List


def solution(numbers: List[int], target: int):
    count = 0

    def dfs(index: int, csum: int):
        """
        Args:
            index: 몇 번째 numbers 차례인지
            csum: 현재까지 숫자들의 총합
        """
        nonlocal count
        if index == len(numbers):
            if csum == target:
                count += 1
            return

        dfs(index + 1, csum + numbers[index])
        dfs(index + 1, csum - numbers[index])

    dfs(0, 0)

    return count
