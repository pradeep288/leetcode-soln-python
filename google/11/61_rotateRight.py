class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head

        list_len = 0
        cur = head
        while cur:
            cur = cur.next
            list_len += 1

        k = k % list_len

        if k == 0:
            return head

        cur = head
        idx = 0
        while idx < len(list_len) - k:
            cur = cur.next
            idx += 1

        new_head = cur.next

        new_cur = new_head
        cur.next = None
        while cur and cur.next:
            cur = cur.next

        cur.next = head

        head = new_head

        return head
