class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        d = {}
        res = []
        for i, s in enumerate(strs):
            key = self.make_key(s)
            # First occurence of an anagram
            if key not in d:
                d[key] = [s]
            else:
                d[key].append(s)
        for key in d:
            if len(d[key]) > 1:
                res += d[key]
        return res

    def make_key(self, s):
        """Generate character-frequency key based on s"""
        d = {}
        res = []
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        # Iterate form 'a' to 'z'
        # This make sure the character occurences is ordered
        # and thus unique
        for i in range(ord('a'), ord('z') + 1):
            c = chr(i)
            if c in d:
                res.append(c)
                res.append(str(d[c]))
        return ''.join(res)
