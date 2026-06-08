class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = set()
        def dfs(i, j, index):
            if index == len(word):
                return True
            if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or (i, j) in visited or board[i][j] != word[index]:
                return False
            
            visited.add((i, j))
            res = dfs(i + 1, j, index + 1) or dfs(i - 1, j, index + 1) or dfs(i, j + 1, index + 1) or dfs(i, j - 1, index + 1)
            visited.remove((i, j))
            return res

        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False