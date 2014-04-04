class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        n = len(num)
        k = -1
        # Find the largest k such that num[k] < num[k + 1]
        for i in range(n - 1):
            if num[i] < num[i + 1]:
                k = i

        # Find the largest l such that num[k] < num[l]
        l = -1
        if k >= 0:
            for i in range(n):
                if num[i] > num[k]:
                    l = i  # l must exist if k >= 0

        # Swap num[k] and num[l]
        num[k], num[l] = num[l], num[k]

        # Reverse num[k + 1:n]
        l = k + 1
        r = n - 1
        while l < r:
            num[l], num[r] = num[r], num[l]
            l += 1
            r -= 1
        return num
