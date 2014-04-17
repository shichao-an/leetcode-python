class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        l = r = n
        one = ''
        stack = []
        res = []
        self.gp(stack, l, r, one, res)
        return res

    def gp(self, stack, l, r, one, res):
        if l == 0 and r == 0:
            res.append(one)
        else:
            if not stack:
                if l > 0:
                    stack.append('(')
                    one += '('
                    self.gp(stack, l - 1, r, one, res)
                    stack.pop()
                    one = one[:-1]
            else:
                if l > 0:
                    one += '('
                    stack.append('(')
                    self.gp(stack, l - 1, r, one, res)
                    stack.pop()
                    one = one[:-1]
                if r > 0:
                    stack.pop()
                    one += ')'
                    self.gp(stack, l, r - 1, one, res)
                    stack.append('(')
                    one = one[:-1]
