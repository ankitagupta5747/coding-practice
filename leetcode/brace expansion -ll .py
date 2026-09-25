class Solution:
    def braceExpansionII(self, expression):
        def parse(s):
            result = {""}
            i = 0

            while i < len(s):
                if s[i] == '{':
                    count = 1
                    j = i + 1

                    while count:
                        if s[j] == '{':
                            count += 1
                        elif s[j] == '}':
                            count -= 1
                        j += 1

                    inside = s[i + 1:j - 1]
                    parts = split(inside)

                    new_result = set()

                    for a in result:
                        for b in parts:
                            new_result.add(a + b)

                    result = new_result
                    i = j

                else:
                    new_result = set()

                    for x in result:
                        new_result.add(x + s[i])

                    result = new_result
                    i += 1

            return result

        def split(s):
            parts = []
            start = 0
            count = 0

            for i in range(len(s)):
                if s[i] =s= '{':
                    count += 1
                elif s[i] == '}':
                    count -= 1
                elif s[i] == ',' and count == 0:
                    parts.append(s[start:i])
                    start = i + 1

            parts.append(s[start:])
            
            ans = set()

            for part in parts:
                ans.update(parse(part))

            return ans

        return sorted(parse(expression))