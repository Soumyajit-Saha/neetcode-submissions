class Solution:
    def checkMove(self, board: list[list[str]], rMove: int, cMove: int, color: str) -> bool:
        n = len(board)
        m = len(board[0])

        board[rMove][cMove] = color

        def dfs(i, j, i_incr, j_incr):
            i += i_incr
            j += j_incr
            other_color = 'B' if color == 'W' else 'W'
            middle = 0
            while 0 <= i < n and 0 <= j < m and board[i][j] == other_color:
                i += i_incr
                j += j_incr
                middle += 1
            if i == n or i == -1 or j == m or j == -1 or board[i][j] == '.':
                return False
            return board[i][j] == color and middle > 0

        return dfs(rMove, cMove, 1, 0) or dfs(rMove, cMove, 0, 1) or dfs(rMove, cMove, -1, 0) or dfs(rMove, cMove, 0, -1) or dfs(rMove, cMove, -1, -1) or dfs(rMove, cMove, 1, 1) or dfs(rMove, cMove, 1, -1) or dfs(rMove, cMove, -1, 1)