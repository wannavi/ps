# [1,2,4], target = 3 or 5
# 0 2 => 2 2 => target이 더 작은 경우 left, 아닌 경우 left + 1

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        return left
