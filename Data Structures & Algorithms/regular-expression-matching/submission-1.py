class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}

        def dfs(i, j):
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False

            if (i, j) in dp:
                return dp[(i, j)]

            if j + 1 < len(p) and p[j + 1] == '*':
                # we can omit check for s[i] with p[j]* 
                # or if s[i] == p[j] or p[i] == '.', we can match more elements from s[i] to p[j]*
                dp[(i, j)] = dfs(i, j + 2) or ((i < len(s) and (s[i] == p[j] or p[j] == '.')) and dfs(i + 1, j))
                return dp[(i, j)]

            if i < len(s) and (s[i] == p[j] or p[j] == '.'):
                dp[(i, j)] = dfs(i + 1, j + 1)
                return dp[(i, j)]

            dp[(i, j)] = False
            return dp[(i, j)]


        return dfs(0, 0)
