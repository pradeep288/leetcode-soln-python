class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next

        res = 0
        idx = 0

        for num in arr[::-1]:
            res = res + num * 2 ** idx
            idx += 1

        return res
