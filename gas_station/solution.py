class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        t = [0 for i in range(n)]
        for i in range(n):
            t[i] = gas[i] - cost[i]
        res = 0
        cs = 0  # Current sum
        ts = 0  # Total sum
        for i in range(n):
            cs += t[i]
            ts += t[i]
            if cs < 0:
                res = i + 1
                cs = 0
        if ts < 0:
            return -1
        else:
            return res

    def canCompleteCircuit2(self, gas, cost):
        # Brute-force
        n = len(gas)
        for i in range(n):
            if gas[i] - cost[i] < 0:
                continue
            carry = gas[i] - cost[i]
            j = (i + 1) % n
            flag = True
            while j != i % n:
                if carry + gas[j] - cost[j] < 0:
                    flag = False
                    break
                j = (j + 1) % n
            if flag:
                return i
        return -1


s = Solution()
print s.canCompleteCircuit2([2, 4], [3, 4])
