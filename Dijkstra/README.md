## 최단경로 알고리즘 중 하나인 다익스트라 알고리즘..

- 이 알고리즘이 하는 일은 그래프의 어떤 정점 하나를 시작점으로 선택하고, 나머지 정점들로의 최단거리를 모두 구합니다.
  - 정점 개수가 V, 간선 개수가 E일 때 기본적인 최적화를 거치면 **O(ElogV)**의 시간복잡도를 갖습니다.
  - 그래프는 무향이거나 유향인데 대체로 유향인 경우가 많고, 간선마다 이동거리가 존재합니다.
  - 또한 모든 거리값이 **음수가 아닐 때만** 사용할 수 있습니다.
    - 만약 음수 값이 있다면 벨만 포드처럼 음수 가중치를 처리할 수 있는 알고리즘을 쓰거나, 모두 값을 더해 양수로 변환하는 방법을 써야 합니다.
- 다익스트라의 최초 구현에서는 시간 복잡도가 O(V^2)이었는데 우선순위 큐를 도입하여 O(V+ElogV)가 되었으니, 우선순위 큐에 대해서도 알아봅시다.
  - 매 노드마다 O(V)이고, 루프는 V-1번 실행되므로 O(V^2)의 시간복잡도가 발생합니다.

## 작동원리

1. 아직 방문하지 않은 정점들 중 거리가 가장 짧은 정점을 하나 선택해 방문한다.
2. 해당 정점에서 인접하고 아직 방문하지 않은 정점들의 거리를 갱신한다.

## 수도 코드

```
function Dijkstra(Graph, source):
	dist[source] <- 0
	
	create vertex priority queue Q
	
	for each vertex v in Graph:
		if v != source
			dist[v] <- INFINITY
			prev[v] <- UNDEFINED
			
		Q.add_with_priority(v, dist[v])
  
  while Q is not empty:
  	u <- Q.extract_min()
  	for each neighbor v of u:
  		alt <- dist[u] + length(u, v)
  		if alt < dist[v]
  			dist[v] <- alt
  			prev[v] <- u
  			Q.decreased_priority(v, alt)
  			
  return dist, prev
```

