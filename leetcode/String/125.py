from collections import deque


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # pythonic
        sv = [ch for ch in s.lower() if ch.isalnum()]
        return sv == sv[::-1]

    def isPalindrome1(self, s: str) -> bool:
        # two pointer
        s = s.lower()
        l, r = 0, len(s) - 1

        while l < r:
            a, b = s[l], s[r]
            if a.isalnum() and b.isalnum():
                if a != b:
                    return False
                else:
                    i, j = i + 1, j - 1
                    continue
            l, r = l + (not a.isalnum()), j - (not b.isalnum())

        return True

    def isPalindrome2(self, s: str) -> bool:
        strs = deque([ch for ch in s.lower() if ch.isalnum()])

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True
