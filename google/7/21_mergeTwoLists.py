class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        dummy_node = ListNode(0, None)
        cur_node = dummy_node
        while list1 and list2:
            if list1.val <= list2.val:
                cur_node.next = list1
                list1 = list1.next
            else:
                cur_node.next = list2
                list2 = list2.next
            cur_node = cur_node.next

        if list1:
            cur_node.next = list1
        elif list2:
            cur_node.next = list2

        return dummy_node.next
