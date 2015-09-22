"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        res = 0
        for i, c in enumerate(s):
            if i < len(s) - 1 and roman[c] < roman[s[i + 1]]:
                res -= roman[c]
            else:
                res += roman[c]
        return res
