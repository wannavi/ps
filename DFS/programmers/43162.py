from typing import List
from collections import deque


def solution(n: int, computers: List[List[int]]):
    count = 0
    vis = [False] * n

    for i in range(n):
        if not vis[i]:
            bfs(computers, vis, i)
            count += 1

    return count


def bfs(graph: List[List[int]], vis: List[int], here: int):
    q = deque([here])
    vis[here] = True

    while q:
        v = q.popleft()
        for w, ok in enumerate(graph[v]):
            if ok and not vis[w]:
                q.append(w)
                vis[w] = True
