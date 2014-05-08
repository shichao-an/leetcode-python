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
