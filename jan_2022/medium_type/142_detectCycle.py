class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        # Part 1: Check if Cycle Exists
        sp, fp = head, head

        while fp is not None and fp.next is not None:
            sp = sp.next
            fp = fp.next.next
            if sp == fp:
                break

        if fp is None or fp.next is None:
            return None

        # Part 2: Cycle Exists and find the start of the cycle from head.
        fp = head

        while sp != fp:
            sp = sp.next
            fp = fp.next

        return fp
