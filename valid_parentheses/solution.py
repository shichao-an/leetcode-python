"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid
but "(]" and "([)]" are not.
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pars = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        stack = []
        for c in s:
            # Left parenthesis
            if c not in pars:
                stack.append(c)
            # Right parenthesis
            else:
                if stack:
                    if stack[-1] == pars[c]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if stack:
            return False
        else:
            return True
