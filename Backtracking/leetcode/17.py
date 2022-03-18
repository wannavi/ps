class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        result = []
        digit_to_chars = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return

            for ch in digit_to_chars[digits[index]]:
                dfs(index + 1, path + ch)

        dfs(0, '')

        return result
