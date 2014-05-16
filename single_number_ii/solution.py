class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        # Assume 32-bit integer
        num_of_bits = 32  # Change this to 64 on 64-bit platform
        res_bit = 0
        res = 0
        # First check whether the single number is negative
        for num in A:
            bit = 1 if num & (1 << (num_of_bits - 1)) != 0 else 0
            res_bit = (res_bit + bit) % 3
        positive = True if res_bit == 0 else False

        for i in range(num_of_bits - 1):
            res_bit = 0
            # For each bit of each number, calculate each bit
            # of the single number
            for num in A:
                bit = 1 if num & (1 << i) != 0 else 0
                res_bit = (res_bit + bit) % 3
            # If single number is positive
            if positive and res_bit == 1:
                res += 1 << i
            # If single number is negative
            if not positive and res_bit == 0:
                res += 1 << i
        if not positive:
            res = -(res + 1)
        return res
