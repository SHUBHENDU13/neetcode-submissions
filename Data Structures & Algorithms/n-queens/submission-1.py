class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for i in range(n)]

        cols = set()
        posdiag = set()
        negdiag = set()

        def backtrack(r):
            if r == n:
                copy = [''.join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in cols or (r + c) in posdiag or (r - c) in negdiag:
                    continue

                cols.add(c)
                posdiag.add(r + c)
                negdiag.add(r - c)
                board[r][c] = 'Q'

                backtrack(r + 1)
                
                cols.remove(c)
                posdiag.remove(r + c)
                negdiag.remove(r - c)
                board[r][c] = '.'

        backtrack(0)
        return res