class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(path: List[int] = []):
            if len(path) == len(nums):
                result.append(path)
                return

            for n in nums:
                if n not in path:
                    dfs([*path, n])

        dfs()

        return result
