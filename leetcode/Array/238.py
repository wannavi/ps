class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul, zero_count = 1, 0
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                mul *= num

        if zero_count > 1:
            return [0] * len(nums)
        else:
            if zero_count = 1:
                return [mul if num == 0 else 0 for num in nums]
            else:
                return [mul // num for num in nums]

    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        out = []
        p = 1

        # 왼쪽 곱셈
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]

        p = 1
        # 왼쪽 곱셈 결과에 오른쪽 곱셈
        for i in range(len(nums) - 1, 0 - 1, -1):
            out[i] = out[i] * p
            p = p * nums[i]

        return out
