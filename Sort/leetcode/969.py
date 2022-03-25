class Solution:
    def pancakeSort(self, arr):
        result = []
        n = len(arr)

        while n:
            idx = 0
            for i in range(n):
                if arr[i] > arr[idx]:
                    idx = i

            # 이미 맨 뒤가 가장 큰 상태일때
            if idx == n - 1:
                n -= 1
                continue

            # reversed가 있지만 더 느려서..
            self.reverse(arr, 0, idx)
            self.reverse(arr, 0, n - 1)
            result = [*result, idx + 1, n]

            n -= 1

        return result

    def reverse(self, arr, st, ed):
        for i in range((st+ed)//2 + 1):
            arr[st+i], arr[ed-i] = arr[ed-i], arr[st+i]
