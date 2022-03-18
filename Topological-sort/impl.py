import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacent = collections.defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            adjacent[a].append(b)
            indegree[b] += 1

        q = collections.deque()

        # 1. indegree가 0인 node 넣기
        for idx, val in enumerate(indegree):
            if val == 0:
                q.append(idx)

        # 2. topological sort - 중간에 나온다면 cycle 존재 한다는 것
        for _ in range(numCourses):
            if not q:
                return False

            curr = q.popleft()
            for w in adjacent[curr]:
                indegree[w] -= 1
                if indegree[w] == 0:
                    q.append(w)

        return True
