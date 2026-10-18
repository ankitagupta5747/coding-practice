class Solution:
    def climbStairs(self, n):
        a = 1
        b = 1

        for i in range(n - 1):
            a, b = b, a + b

        return b