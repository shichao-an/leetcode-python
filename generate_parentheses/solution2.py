class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        cand = []
        res = []
        self.generate_paren_aux(n, n, cand, res)
        return res

    def generate_paren_aux(self, left, right, cand, res):
        if left == 0 and right == 0:
            res.append(''.join(cand))
        else:
            if left <= right and left > 0:
                cand.append('(')
                self.generate_paren_aux(left - 1, right, cand, res)
                cand.pop()
            if left < right and right > 0:
                cand.append(')')
                self.generate_paren_aux(left, right - 1, cand, res)
                cand.pop()
