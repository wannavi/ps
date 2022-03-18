# 시간초과 풀이
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))

        # 우선순위 큐: [(비용, 정점, 이동횟수)]
        Q = [(0, src, -1)]
        # dist: [(가격, 이동횟수)]
        dist = collections.defaultdict(list)

        while Q:
            price, node, steps = heapq.heappop(Q)
            if steps <= k:
                dist[node].append((price, steps))
                for v, w in adj[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, steps + 1))

        result = [price for price, step in dist[dst] if step <= k]
        return min(result) if result else -1
