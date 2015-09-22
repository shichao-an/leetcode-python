"""
Given a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        current = head
        last = None
        count = 0  # Repeated count of `last`
        dummy = ListNode(0)
        dummy_end = dummy
        while current is not None:
            if last is not None:
                if current.val == last.val:
                    count += 1
                else:
                    if count == 0:
                        dummy_end.next = last
                        dummy_end = last
                    count = 0
            last = current
            current = current.next
        if count == 0:
            dummy_end.next = last
            dummy_end = last
        dummy_end.next = None
        return dummy.next
