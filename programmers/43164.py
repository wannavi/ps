from collections import defaultdict


def solution(tickets):
    graph = make_graph(tickets)
    path = []

    def dfs(w):
        while graph[w]:
            dfs(graph[w].pop(0))
        path.append(w)

    dfs("ICN")

    return path[::-1]


def make_graph(tickets):
    graph = defaultdict(list)
    for k, v in sorted(tickets):
        graph[k].append(v)

    return graph
