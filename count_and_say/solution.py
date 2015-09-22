"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ln = list(str(1))
        for i in range(1, n):
            tn = []
            count = 1
            prev = None
            for c in ln:
                if prev == c:
                    count += 1
                if prev is not None and prev != c:
                    tn.append(str(count))
                    tn.append(str(prev))
                    count = 1
                prev = c
            tn.append(str(count))
            tn.append(str(prev))
            ln = tn
        return ''.join(ln)


s = Solution()
print s.countAndSay(1)
print s.countAndSay(2)
print s.countAndSay(3)
print s.countAndSay(4)
print s.countAndSay(5)
