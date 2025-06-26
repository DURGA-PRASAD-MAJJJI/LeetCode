
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def solve(col, board, res, left, low, upper):
            if col == n:
                res.append(["".join(row) for row in board])
                return
            for row in range(n):
                if left[row] == 0 and low[row + col] == 0 and upper[n - 1 + col - row] == 0:
                    board[row][col]='Q'
                    left[row]=1
                    low[row+col]=1
                    upper[n-1+col-row]=1
                    solve(col+1,board,res, left, low, upper)
                    board[row][col] = '.'
                    left[row] = 0
                    low[row + col] = 0
                    upper[n - 1 + col - row] = 0
        board = [['.' for _ in range(n)] for _ in range(n)]
        res = []
        left = [0] * n
        low = [0] * (2 * n - 1)
        upper = [0] * (2 * n - 1)
        solve(0, board, res, left, low, upper)
        return res
