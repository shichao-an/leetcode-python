"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = []
        # a is longer than b
        if len(a) < len(b):
            b, a = a, b
        n = len(a)
        m = len(b)
        c = 0  # Carry bit
        r = 0  # Result bit
        # i = n - 1 ... 0
        for k in range(n):
            i = n - 1 - k
            if k < m:
                j = m - 1 - k
                r = (int(a[i]) + int(b[j]) + c) % 2
                c = (int(a[i]) + int(b[j]) + c) / 2
            else:
                r = (int(a[i]) + c) % 2
                c = (int(a[i]) + c) / 2
            res.insert(0, str(r))
        if c == 1:
            res.insert(0, str(c))
        return ''.join(res)
