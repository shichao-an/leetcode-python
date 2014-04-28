class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        res = []
        for i in range(len(num) - 2):
            if i == 0 or i > 0 and num[i - 1] != num[i]:
                left = i + 1
                right = len(num) - 1
                while left < right:
                    s = num[i] + num[left] + num[right]
                    if s == 0:
                        res.append([num[i], num[left], num[right]])
                        left += 1
                        right -= 1
                        while left < right and num[left] == num[left - 1]:
                            left += 1
                        while right > left and num[right] == num[right + 1]:
                            right -= 1
                    elif s < 0:
                        left += 1
                    else:
                        right -= 1
        return res
