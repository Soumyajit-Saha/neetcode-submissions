class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        dp = {}
        for i in range(len(s)):
            dp[(i, i)] = True
        res = []
        comb = []

        def isPalindrome(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if j < i:
                return True
            if s[i] == s[j]:
                dp[(i, j)] = isPalindrome(i + 1, j - 1)
            else:
                dp[(i, j)] = False
            return dp[(i, j)]

        def dfs(index):
            if index == len(s):
                res.append(comb.copy())
                return
            for end in range(index, len(s)):
                if isPalindrome(index, end):
                    comb.append(s[index: end + 1])
                    dfs(end + 1)
                    comb.pop()
        
        dfs(0)
        return res
            
