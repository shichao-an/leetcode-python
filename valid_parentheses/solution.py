class Solution:
    # @return a boolean
    def isValid(self, s):
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
