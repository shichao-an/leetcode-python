"""
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.

Notes:
* You must use only standard operations of a stack -- which means only push to
top, peek/pop from top, size, and is empty operations are valid.
* Depending on your language, stack may not be supported natively. You may
simulate a stack by using a list or deque (double-ended queue), as long as you
use only standard operations of a stack.
* You may assume that all operations are valid (for example, no pop or peek
operations will be called on an empty queue).
"""

class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []  # Push
        self.stack2 = []  # Pop

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack1.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if not self.stack2:
            self._move()
        self.stack2.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.stack2:
            self._move()
        return self.stack2[-1]

    def empty(self):
        """
        :rtype: bool
        """
        if not self.stack2:
            self._move()
        if not self.stack2:
            return True
        else:
            return False

    def _move(self):
        """Move elements from stack1 to stack2"""
        while self.stack1:
            self.stack2.append(self.stack1.pop())
