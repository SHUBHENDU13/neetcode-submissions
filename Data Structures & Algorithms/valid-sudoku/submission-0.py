class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = 9, 9
        row = {i:set() for i in range(ROWS)}
        col = {i:set() for i in range(COLS)}

        grids = [[0,0], [0,3], [0,6], [3,0], [3,3], [3,6], [6,0], [6,3], [6,6]]
        local_grid = {tuple(i):set() for i in grids}

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c].isdigit() and board[r][c] in row[r]:
                    return False
                if board[r][c].isdigit():
                    row[r].add(board[r][c])
        
        for c in range(COLS):
            for r in range(ROWS):
                if board[r][c].isdigit() and board[r][c] in col[c]:
                    return False
                if board[r][c].isdigit():
                    col[c].add(board[r][c])

        for r_orig, c_orig in grids:
            start_r, start_c = r_orig, c_orig
            r_bound, c_bound = r_orig + 3, c_orig + 3
            r = start_r
            while r < r_bound:
                c = start_c
                while c < c_bound:
                    if board[r][c].isdigit() and board[r][c] in local_grid[(start_r, start_c)]:
                        return False
                    if board[r][c].isdigit():
                        local_grid[(start_r, start_c)].add(board[r][c])
                    c += 1
                r += 1
        
        return True
