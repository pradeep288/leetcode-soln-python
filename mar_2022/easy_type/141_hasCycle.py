class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        sp = head
        fp = head
        while fp is not None and fp.next is not None:
            sp = sp.next
            fp = fp.next.next

            if sp == fp:
                return True

        return False
