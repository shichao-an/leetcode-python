class Solution:
    # @return an integer
    def romanToInt(self, s):
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        prefixes = {
            'I': ('V', 'X'),
            'X': ('L', 'C'),
            'C': ('D', 'M'),
        }
        # Stack for storing prefixes
        stack = []
        res = 0
        for c in s:
            if c not in prefixes:
                if stack:
                    # Subtract prefixes in stack
                    if c in prefixes[stack[0]]:
                        while stack:
                            res -= roman[stack.pop()]
                    else:
                        while stack:
                            res += roman[stack.pop()]
                res += roman[c]
            else:
                if stack:
                    if stack[0] == c:
                        stack.append(c)
                    else:
                        if c in prefixes[stack[0]]:
                            while stack:
                                res -= roman[stack.pop()]
                        else:
                            while stack:
                                res += roman[stack.pop()]
                        stack.append(c)
                else:
                    stack.append(c)
        while stack:
            res += roman[stack.pop()]
        return res
