# 위상 정렬

- "위상 정렬을 구현하는 가장 직관적인 방법은 들어오는 간선이 하나도 없는 정점들을 하나씩 찾아서 정렬 결과의 뒤에 붙이고, 그래프에서 이 정점을 지우는 과정을 반복하는 것입니다."
  - 큐에다가 indegree=0인 정점들을 집어넣고, 반복하면 되는 것입니다.
  
