from typing import List


N, M = map(int, input().split())
result = []


def dfs(next_elements: List[int], path: List[int] = []):
    if len(path) == M:
        result.append(path)
        return

    for idx, elem in enumerate(next_elements):
        _next_elements = next_elements[:]
        _next_elements.remove(elem)
        dfs(_next_elements, [*path, elem])


dfs(list(range(1, N + 1)))
for vec in result:
    print(' '.join(map(str, vec)))
