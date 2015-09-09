"""
Given two numbers represented as strings, return multiplication of the numbers
as a string.

Note: The numbers can be arbitrarily large and are non-negative.
"""


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        a = num1[::-1]
        b = num2[::-1]
        n = len(a)
        m = len(b)
        res = ['0' for i in range(n + m)]
        for i in range(n):
            c = 0
            for j in range(m):
                tmp = int(a[i]) * int(b[j]) + int(res[i + j]) + c
                digit = tmp % 10
                res[i + j] = str(digit)
                c = tmp / 10
            if c > 0:
                res[m + i] = str(c)
        res = ''.join(res[::-1])
        for i, d in enumerate(res):
            if d != '0':
                return res[i:]
        else:
            return '0'

s = Solution()

print s.multiply('2', '21')
print s.multiply('83', '3')
