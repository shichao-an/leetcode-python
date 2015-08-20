class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        size = 32
        for i in range(size):
            if self.test_bit(n, i):
                print(i)
                res = self.set_bit(res, size - 1 - i)
        return res

    def test_bit(self, n, i):
        mask = 1 << i
        if n & mask > 0:
            return True
        return False

    def set_bit(self, n, i):
        mask = 1 << i
        return n | mask

s = Solution()
print(bin(43261596))
res = s.reverseBits(43261596)
print(bin(res))
