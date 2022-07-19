class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        list_len = 0
        cur = head
        while cur:
            cur = cur.next
            list_len += 1

        cur = head
        count = k
        while count > 1:
            cur = cur.next
            count -= 1
        kth_node = cur

        cur = head
        count = list_len - k
        while count > 0:
            cur = cur.next
            count -= 1

        cur.val, kth_node.val = kth_node.val, cur.val

        return head
