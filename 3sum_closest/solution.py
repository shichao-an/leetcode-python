class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        n = len(num)
        res = num[0] + num[1] + num[2]
        for i in range(n - 2):
            l = i + 1
            r = n - 1
            while l < r:
                s = num[i] + num[l] + num[r]
                if abs(s - target) < abs(res - target):
                    res = s
                if s == target:
                    return s
                elif s < target:
                    l += 1
                else:
                    r -= 1
        return res
