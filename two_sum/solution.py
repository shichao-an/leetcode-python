class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        d = {}
        for i, e in enumerate(num):
            if e in d:
                return d[e] + 1, i + 1
            d[target - e] = i
