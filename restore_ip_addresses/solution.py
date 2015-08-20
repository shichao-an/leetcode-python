"""
Given a string containing only digits, restore it by returning all possible
valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""

class Solution:
    # @param {string} s
    # @return {string[]}
    def restoreIpAddresses(self, s):
        res = []
        cand = []
        self.restore_ip(s, cand, res)
        return res

    def restore_ip(self, s, cand, res):
        # If more than 4 parts, or 4 parts already but with remaining
        # unprocessed sub-string
        if len(cand) > 4 or len(cand) == 4 and s:
            return
        elif not s and len(cand) == 4:
                res.append('.'.join(cand))
        else:
            k = min(3, len(s))  # Ensures s[:j + 1] won't be duplicate
            for j in range(k):
                b = s[:j + 1]
                if self.is_valid_byte(b):
                    cand.append(b)
                    self.restore_ip(s[j + 1:], cand, res)
                    cand.pop()

    def is_valid_byte(self, b):
        if b == '0':
            return True
        elif b.startswith('0'):
            return False
        else:
            return int(b) < 256

a = "25525511135"
b = "010010"
s = Solution()
print(s.restoreIpAddresses(a))
print(s.restoreIpAddresses(b))
