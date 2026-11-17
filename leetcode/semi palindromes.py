class Solution:
    def minimumChanges(self, s, k):
        n = len(s)
        cost = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                best = n

                for d in range(1, length):
                    if length % d == 0:
                        count = 0

                        for x in range(d):
                            l = i + x
                            r = j - d + 1 + x

                            while l < r:
                                if s[l] != s[r]:
                                    count += 1

                                l += d
                                r -= d

                        best = min(best, count)

                cost[i][j] = best

        dp = [[n] * (k + 1) for _ in range(n + 1)]
        dp[n][0] = 0

        for i in range(n - 1, -1, -1):
            for j in range(1, k + 1):
                for end in range(i + 1, n):
                    dp[i][j] = min(
                        dp[i][j],
                        dp[end + 1][j - 1] + cost[i][end]
                    )

        return dp[0][k]