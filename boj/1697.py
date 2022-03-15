from collections import deque


N, K = map(int, input().split())
dist = [-1] * 100005
dist[N] = 0

queue = deque()
queue.append(N)

while dist[K] == -1:
    n = queue.popleft()

    for next in (n - 1, n + 1, 2 * n):
        if next < 0 or next > 100000:
            continue
        if dist[next] != -1:
            continue

        dist[next] = dist[n] + 1
        queue.append(next)

print(dist[K])
