class Solution:
    def uniquePaths(self, grid):
        MOD = 10**9 + 7

        dp = [1] + [0] * (len(grid[0]) - 1)

        for row in grid:
            res = 0

            for j, x in enumerate(row):

                if x == 1:
                    res, dp[j] = dp[j], res

                else:
                    res = (res + dp[j]) % MOD
                    dp[j] = res

        return res 