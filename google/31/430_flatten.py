class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        dummy = Node()
        dummy.next = head
        head.prev = dummy

        cur, stack = dummy, [head]
        while stack:
            temp = stack.pop()
            if temp.next:
                stack.append(temp.next)
            if temp.child:
                stack.append(temp.child)
            cur.next = temp
            temp.prev = cur
            temp.child = None
            cur = temp
        cur.next = None
        dummy.next.prev = None

        return dummy.next
