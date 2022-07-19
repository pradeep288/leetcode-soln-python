class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sp, fp = head, head

        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next

            if sp == fp:
                return True
        return False
