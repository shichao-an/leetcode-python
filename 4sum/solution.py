# Time Limit Exceeded
class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        n = len(num)
        num.sort()
        res = []
        for a in range(n - 3):
            if a > 0 and num[a - 1] == num[a]:
                continue
            for b in range(a + 1, n - 2):
                if b > a + 1 and num[b - 1] == num[b]:
                    continue
                c = b + 1
                d = n - 1
                while c < d:
                    s = num[a] + num[b] + num[c] + num[d]
                    if s == target:
                        res.append([num[a], num[b], num[c], num[d]])
                        c += 1
                        d -= 1
                        while c < d and num[c] == num[c - 1]:
                            c += 1
                        while c < d and num[d] == num[d + 1]:
                            d -= 1
                    elif s < target:
                        c += 1
                    else:
                        d -= 1
        return res
