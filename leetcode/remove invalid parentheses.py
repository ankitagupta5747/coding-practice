class Solution:
    def removeInvalidParentheses(self, s):
        result = []

        def isValid(x):
            count = 0

            for ch in x:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        def backtrack(index, path):
            if index == len(s):
                x = "".join(path)

                if isValid(x):
                    result.append(x)

                return

            path.append(s[index])
            backtrack(index + 1, path)
            path.pop()

            if s[index] in "()":
                backtrack(index + 1, path)

        backtrack(0, [])

        # Remove duplicates
        result = list(set(result))

        # Keep only minimum removals
        max_len = max(len(x) for x in result)
        result = [x for x in result if len(x) == max_len]

        return result