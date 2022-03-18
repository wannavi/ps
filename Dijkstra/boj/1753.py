import collections
import heapq

V, E = map(int, input().split())
K = int(input())

graph = collections.defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


# heapq: [(거리, 정점)]
Q = [(0, K)]
dist = collections.defaultdict(int)

# 가까운 정점 순으로 방문
while Q:
    length, node = heapq.heappop(Q)
    if node not in dist:
        dist[node] = length
        for v, w in graph[node]:
            alt = length + w
            heapq.heappush(Q, (alt, v))


for i in range(1, V + 1):
    if i not in dist:
        print('INF')
    else:
        print(dist[i])
