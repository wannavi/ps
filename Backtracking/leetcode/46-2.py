class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(nexts: List[int], path: List[int] = []):
            if not nexts:
                result.append(path)
                return

            for n in nexts:
                _nexts = nexts[:]
                _nexts.remove(n)
                dfs(_nexts, [*path, n])

        dfs(nums)

        return result
