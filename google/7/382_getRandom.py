import random


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        cur = head
        self.count = 0
        while cur:
            cur = cur.next
            self.count += 1

    def getRandom(self) -> int:
        cur = self.head
        res = cur.val

        while cur:
            if random.randrange(0, 2) <= 0:
                res = cur.val
            cur = cur.next

        return res
