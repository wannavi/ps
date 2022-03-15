from collections import defaultdict, deque


n, m, v = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    st, en = map(int, input().split())
    graph[st].append(en)
    graph[en].append(st)


def BFS(v, graph):
    queue = deque([v])
    visited = [v]

    while queue:
        v = queue.popleft()
        for w in sorted(graph[v]):
            if w not in visited:
                visited.append(w)
                queue.append(w)

    return visited


def DFS(v, graph):
    stack = [v]
    visited = []

    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for w in sorted(graph[v], reverse=True):
                stack.append(w)

    return visited


for k in DFS(v, graph):
    print(k, end=' ')

print()

for k in BFS(v, graph):
    print(k, end=' ')
