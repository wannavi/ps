from typing import List


def solution(n: int, info: List[int]) -> List[int]:
    # 1. 아피치보다 작게 쏠거면 아예 x
    # 2. 그러면 needed 만큼 맞춰야함..
    # 3. needed 에서 조합해서 가장 큰 점수 나오도록 하면 됨.

    # 득점을 위해 필요한 최소 개수
    # 6점 획득 하려면 needed[6]개 맞아야함.
    needed = {10 - i: k + 1 for i, k in enumerate(info)}
    target = sum([10 - i for i, v in enumerate(info) if v > 0])
    print(needed)
    print(target)

    # 가능한 조합 찾기 (n 개 쏴서 가능한 경우)
    possible = []
    stack = [(0, [], 0)]  # index(=score), history, count
    while stack:
        score, history, count = stack.pop()
        print(history, sum(history))

        if count == n and sum(history) > target:
            possible.append(history)
        elif count > n or score > 10:
            continue
        else:
            stack.append((score+1, history, count))
            stack.append((score+1, [*history, score], count + needed[score]))

    if not possible:
        return [-1]

    # 합 최대 구하고 그때의 점수 저장
    mx = 0
    for p in possible:
        mx = max(mx, sum(p))
    best_possible = [p for p in possible if sum(p) == mx]

    result = []
    for i in range(10):
        if 10 - i in best_possible:
            result.append(needed[10 - i])
        else:
            result.append(0)

    return result


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
