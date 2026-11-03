class Solution:
    def minMoves(self, nums):
        mx = max(nums)
        total = sum(nums)
        n = len(nums)

        return mx * n - total