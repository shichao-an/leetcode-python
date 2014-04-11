class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        n = len(digits)
        carry = 1
        # From n - 1 to 0
        for i in range(n - 1, - 1, -1):
            if carry + digits[i] > 9:
                digits[i] = (carry + digits[i]) % 10
                carry = 1
            else:
                digits[i] = carry + digits[i]
                carry = 0

        if carry == 1:
            digits.insert(0, 1)
        return digits
