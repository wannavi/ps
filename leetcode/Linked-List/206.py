class Solution:
    def reverseList(self, head):
        def reverse(node, prev):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)

    def reverseList1(self, head):
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev
