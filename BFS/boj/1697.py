from collections import deque


MAX_SIZE = 100005

# next => x-1 or x-2 or x*2
n, k = map(int, input().split())
dist = [-1] * MAX_SIZE

queue = deque()
queue.append(n)
dist[n] = 0

# while 조건을 이렇게 쓴 걸 주목하자.
while dist[k] == -1:
    v = queue.popleft()
    for w in (v-1, v+1, 2*v):
        if w < 0 or w >= MAX_SIZE:
            continue
        if dist[w] != -1:
            continue
        dist[w] = dist[v] + 1
        queue.append(w)

print(dist[k])
