"""
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

"""

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        ls = list(s)
        # C-like processing
        # Process spaces
        i = 0
        j = len(s) - 1
        while i <= j:
            if ls[i] != ' ' and ls[j] != ' ':
                break
            if ls[i] == ' ':
                i += 1
            if ls[j] == ' ':
                j -= 1
        start = i
        end = j
        # Remove duplicate spaces between words
        k = start  # Last processed
        for p in range(start, end + 1):
            if p > start and ls[p] == ' ' and ls[p] == ls[p - 1]:
                pass
            else:
                ls[k] = ls[p]
                k += 1
        end = k - 1
        # Now start..end is the processed array of characters

        # Reverse all characters between start and end
        self.reverse(ls, start, end)

        # Reverse each word
        ws = start  # Word start index
        we = start  # Word end index
        for i in range(start, end + 1):
            if ls[i] == ' ' or i == end:
                we = end if i == end else i - 1
                self.reverse(ls, ws, we)
                ws = i + 1
        return ''.join(ls[start:end + 1])

    def reverse(self, a, i, j):
        while i < j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

    def reverseWords2(self, s):
        cs = list(s)  # Make a C-string like list
        n = len(cs)
        # Remove leading and trailing spaces
        left = 0
        right = n - 1
        while left <= right and (cs[left] == ' ' or cs[right] == ' '):
            if cs[left] == ' ':
                left += 1
            if cs[right] == ' ':
                right -= 1
        # The string contains only spaces
        if left > right:
            return ''
        # Reverse the whole list
        self.reverse(cs, left, right)
        # Remove multiple spaces between two words
        j = left
        for i in range(left, right + 1):
            if cs[i] != ' ' or cs[i] == ' ' and cs[i - 1] != ' ':
                cs[j] = cs[i]
                j += 1
        right = j - 1
        # Reverse each word
        start = left
        q = start
        while q <= right:
            while q <= right and cs[q] != ' ':
                q += 1
            # q - 1 is the end index of the word
            self.reverse(cs, start, q - 1)
            # Start of next word
            start = q
            while start <= right and cs[start] == ' ':
                start += 1
            q = start
        return ''.join(cs[left:right + 1])


s = Solution()
print(s.reverseWords("the sky is blue"))
