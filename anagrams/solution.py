class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        d = {}
        res = []
        for i, s in enumerate(strs):
            ss = ''.join(sorted(s))
            if ss in d:
                if d[ss] >= 0:
                    i = d[ss]
                    res.append(strs[i])  # Append first anagram
                    d[ss] = -1  # Flag this anagram
                res.append(s)
            else:
                d[ss] = i  # Added the index of the first anagram
        return res
