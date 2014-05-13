# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head is None:
            return None
        h = head
        p = h
        while p is not None:
            next_node = p.next
            new_node = RandomListNode(p.label)
            # Insert new node to the original list
            p.next = new_node
            new_node.next = next_node
            p = next_node
        p = h
        while p is not None:
            next_node = p.next.next
            new_node = p.next
            if p.random is not None:
                new_node.random = p.random.next
            p = next_node
        # Split the list
        res = None
        end = None
        p = h
        while p is not None:
            next_node = p.next.next
            new_node = p.next
            # Add to new list
            if res is None:
                res = new_node
                end = new_node
            else:
                end.next = new_node
                end = end.next
            # Delete new node from old list
            p.next = next_node
            p = next_node
        return res
