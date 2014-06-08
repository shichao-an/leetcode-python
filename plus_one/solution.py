class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        digits.reverse()
        res = []
        t = (digits[0] + 1) % 10
        carry = (digits[0] + 1) / 10
        res.append(t)
        for d in digits[1:]:
            t = (d + carry) % 10
            carry = (d + carry) / 10
            res.append(t)
        if carry == 1:
            res.append(1)
        res.reverse()
        return res
