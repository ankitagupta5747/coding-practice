class Solution:
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):

        a = min(need1, need2)
        b = max(need1, need2)

        ans1 = need1 * cost1 + need2 * cost2

        ans2 = a * costBoth + (need1 - a) * cost1 + (need2 - a) * cost2

        ans3 = b * costBoth

        return min(ans1, ans2, ans3)