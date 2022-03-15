class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0

        for i, num in enumerate(nums):
            if i % 2 == 0:
                result += num

        return result

    def arrayPairSum1(self, nums: List[int]) -> int:
        sum, pair = 0, []
        nums.sort()

        for num in nums:
            pair.append(num)
            if len(pair) == 2:
                sum += min(pair)
                pair = []

        return sum

    def arrayPairSum2(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
