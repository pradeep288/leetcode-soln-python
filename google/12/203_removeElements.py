class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_node = ListNode(0)
        dummy_node.next = head
        cur = head
        while cur:
            if cur.val == val:
                dummy_node.next = cur.next
            dummy_node = cur
            cur = cur.next

        return dummy_node.next
