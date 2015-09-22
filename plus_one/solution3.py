"""
Given a non-negative number represented as an array of digits, plus one to the
number.

The digits are stored such that the most significant digit is at the head of
the list.
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = digits[::-1]
        n = len(digits)
        temp = 0
        # Treat "plus one" as the initial carry being 1
        carry = 1
        i = 0
        res = []
        while i < n or carry > 0:
            temp = 0
            if i < n:
                temp += digits[i]
            if carry > 0:
                temp += carry
            digit = temp % 10
            carry = temp / 10
            res.append(digit)
            i += 1
        return res[::-1]

a0 = []
a1 = [3, 3, 5]
a2 = [4, 9, 9]
a3 = [9, 9, 9]
s = Solution()
print s.plusOne(a0)
print s.plusOne(a1)
print s.plusOne(a2)
print s.plusOne(a3)
