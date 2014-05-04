class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        res = []
        cand = []
        self.partition_aux(s, cand, res)
        return res

    def partition_aux(self, s, cand, res):
        if not s:
            res.append(cand[:])
        else:
            for i, e in enumerate(s):
                if self.is_palindrome(s[:i + 1]):
                    cand.append(s[:i + 1])
                    self.partition_aux(s[i + 1:], cand, res)
                    cand.pop()

    def is_palindrome(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
