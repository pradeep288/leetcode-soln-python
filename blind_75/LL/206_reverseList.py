class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        if head and head.next is None:
            return head

        dummy_node = ListNode()
        dummy_node.next = head
        prev, cur, n = dummy_node, head, head.next

        while n:
            cur.next = prev
            prev = cur
            cur = n
            n = n.next

        dummy_node.next.next = None
        cur.next = prev

        return cur
