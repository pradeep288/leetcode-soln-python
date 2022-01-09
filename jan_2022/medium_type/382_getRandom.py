# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# https://www.youtube.com/watch?v=DC2el-eDNi4&ab_channel=TECHDOSE

import random


class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        cur = self.head
        res = cur.val
        count = 1
        while cur:
            r = random.randrange(count)
            if r == 0:
                res = cur.val
            cur = cur.next
            count = count + 1

        return res
# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
