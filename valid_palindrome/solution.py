class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if not s:
            return True
        left = 0
        right = len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
            if not s[right].isalnum():
                right -= 1
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() == s[right].lower():
                    left += 1
                    right -= 1
                else:
                    return False
        return True
