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
        list_a = [int(i) for i in a[::-1]]
        list_b = [int(i) for i in b[::-1]]
        la = len(list_a)
        lb = len(list_b)
        # Pad zeroes
        if la < lb:
            list_a += [0 for i in range(lb - la)]
            la = len(list_a)
        else:
            list_b += [0 for i in range(la - lb)]
            lb = len(list_b)
        carry = 0
        res = []
        for i in range(la):
            t = (list_a[i] + list_b[i] + carry) % 2
            carry = (list_a[i] + list_b[i] + carry) / 2
            res.append(t)
        if carry == 1:
            res.append(1)
        return ''.join([str(d) for d in res[::-1]])
