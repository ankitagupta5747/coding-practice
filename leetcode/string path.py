class Solution:
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        if grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False

        def dfs(i, j, balance):
            if balance < 0:
                return False

            if i == m - 1 and j == n - 1:
                return balance == 0

            if i + 1 < m:
                if dfs(i + 1, j, balance + (1 if grid[i + 1][j] == '(' else -1)):
                    return True

            if j + 1 < n:
                if dfs(i, j + 1, balance + (1 if grid[i][j + 1] == '(' else -1)):
                    return True

            return False

        return dfs(0, 0, 1)