# Bumped!
import collections
import heapq

"""
Args:
    n: #cities
    m: #loads
    f: #flights
    s: start city
    t: end city
"""
n, m, f, s, t = map(int, input().split())

graph = collections.defaultdict(list)
flight = collections.defaultdict(list)
for _ in range(m):
    i, j, c = map(int, input().split())
    graph[i].append((j, c))
    graph[j].append((i, c))

for _ in range(f):
    u, v = map(int, input().split())
    flight[u].append(v)


def dijkstra(graph, st, en):
    # [(비용, 노드)]
    Q = [(0, st)]
    dist = collections.defaultdict(int)

    while Q:
        cost, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = cost
            for j, c in graph[node]:
                alt = cost + c
                heapq.heappush(Q, (alt, j))

    return dist[en]


fees = []
# 비행을 한개씩만 추가해서 최단경로 구해보기?
for u, vs in flight.items():
    for v in vs:
        graph[u].append((v, 0))
        fees.append(dijkstra(graph, s, t))
        graph[u].pop()

print(min(fees))
