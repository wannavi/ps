class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1

        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1

    def mergeTwoLists1(self, l1, l2):
        head = curr = ListNode()

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1, curr = l1.next, curr.next
            else:
                l1, l2 = l2, l1

        if l1 is None:
            l1, l2 = l2, l1

        curr.next = l1

        return head.next
