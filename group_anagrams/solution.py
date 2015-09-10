"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
For the return value, each inner list's elements must follow the lexicographic
order.
All inputs will be in lower-case.

"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        res = []
        for s in strs:
            k = self.make_key(s)
            if k not in d:
                d[k] = [s]
            else:
                d[k].append(s)
        for k in d:
            res.append(sorted(d[k]))
        return res

    def make_key(self, s):
        return ''.join(sorted(s))


s = Solution()
print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
