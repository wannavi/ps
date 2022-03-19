from typing import List, Dict
from collections import defaultdict, deque


# 1. 한단어씩 차이나는 단어들을 잇는 그래프를 만들고
# 2. BFS로 시작과 끝의 최단 경로를 구하면 됨.
def solution(begin: str, target: str, words: List[str]):
    adj = make_graph([begin, *words])

    Q = deque([begin])
    dist = {begin: 0}

    while Q:
        v = Q.popleft()
        for w in adj[v]:
            if w not in dist:
                Q.append(w)
                dist[w] = dist[v] + 1

    return dist[target] if target in dist else 0


def make_graph(words: List[str]) -> Dict[str, str]:
    graph = defaultdict(list)

    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_one_diff(words[i], words[j]):
                graph[words[i]].append(words[j])
                graph[words[j]].append(words[i])

    return graph


def is_one_diff(s1, s2):
    count = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            count += 1

    return True if count == 1 else False
