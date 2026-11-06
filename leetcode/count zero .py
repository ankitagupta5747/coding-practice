class Solution:
    def countServers(self, n, logs, x, queries):
        ans = []

        for q in queries:
            count = set()

            for server, time in logs:
                if q - x <= time <= q:
                    count.add(server)

            ans.append(n - len(count))

        return ans