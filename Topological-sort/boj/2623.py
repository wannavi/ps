from collections import defaultdict, deque

N, M = map(int, input().split())
requests = [list(map(int, input().split())) for _ in range(M)]

adj = defaultdict(list)
indegree = [0] * (N+1)
for req in requests:
    for i in range(1, len(req) - 1):
        adj[req[i]].append(req[i+1])
        indegree[req[i+1]] += 1

# indegree = 0 -> q.append
q, order = deque(), []
for v in range(1, N+1):
    if indegree[v] == 0:
        q.append(v)

is_possible = True
for _ in range(N):
    if not q:
        is_possible = False
        break

    here = q.popleft()
    order.append(here)
    for there in adj[here]:
        indegree[there] -= 1
        if indegree[there] == 0:
            q.append(there)

if is_possible:
    for v in order:
        print(v)
else:
    print(0)
