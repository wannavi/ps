class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        if n - k < k:
            k = n - k

        def dfs(nexts: List[int], path: List[int] = []):
            if len(path) == k:
                result.append(path)
                return

            for idx, n in enumerate(nexts):
                dfs(nexts[idx+1:], [*path, n])

        dfs(list(range(1, n + 1)))

        return result
