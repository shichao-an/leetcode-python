# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head is None:
            return head
        res = None
        res_end = None
        temp = None
        temp_end = None
        i = 1
        while head is not None:
            next_node = head.next
            # Append current node to temp list
            if temp is None:
                temp_end = head
            head.next = temp
            temp = head
            if i % 2 == 0:
                # Append temp to res
                if res is None:
                    res = temp
                    res_end = temp_end
                else:
                    res_end.next = temp
                    res_end = temp_end
                temp = None
            i += 1
            head = next_node
        if temp is not None:
            if res is None:
                res = temp
                res_end = temp_end
            else:
                res_end.next = temp
                res_end = temp_end
        return res
