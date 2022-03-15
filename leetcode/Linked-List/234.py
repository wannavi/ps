from collections import deque


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q = deque()

        if not head:
            return True

        curr = head
        while curr is not None:
            q.append(curr.val)
            curr = curr.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True
