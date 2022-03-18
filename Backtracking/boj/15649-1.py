from typing import List

# discovered 를 쓰는 편이 좋은가?
# 아니면 그냥 쓸 수 있는 배열을 그냥 넘기는게 좋은가?
# 나는 후자가 훨 직관적이라고 생각하긴함.

N, M = map(int, input().split())
discovered = [False] * (N+1)


def dfs(path: List[int] = []):
    if len(path) == M:
        print(' '.join(map(str, path)))
        return

    for i in range(1, N+1):
        if not discovered[i]:
            discovered[i] = True
            path.append(i)
            dfs(path)
            path.pop()
            discovered[i] = False


dfs()
