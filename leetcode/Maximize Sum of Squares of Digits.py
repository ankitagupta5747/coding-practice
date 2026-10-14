class Solution:
    def maxSumOfSquares(self, num, sum):
        if sum > num * 9:
            return ""

        ans = ""

        while sum >= 9:
            ans += "9"
            sum -= 9

        if sum > 0:
            ans += str(sum)

        ans += "0" * (num - len(ans))

        return ans