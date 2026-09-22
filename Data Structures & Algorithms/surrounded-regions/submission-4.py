class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visit = set()

        def dfs(r, c):
            board[r][c] = 'T'
            visit.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or
                    (nr, nc) in visit or board[nr][nc] == 'X'):
                    continue
                dfs(nr, nc)

        # go through every boundary and mark every O cell family as T 
        # so we don't change them
        for r in range(ROWS):
            if board[r][0] == 'O':
                dfs(r, 0)

        for c in range(COLS):
            if board[0][c] == 'O':
                dfs(0, c)

        for r in range(ROWS):
            if board[r][COLS - 1] == 'O':
                dfs(r, COLS - 1)

        for c in range(COLS):
            if board[ROWS - 1][c] == 'O':
                dfs(ROWS - 1, c)

        # go through the entire board and mark X for remaining Os 
        # and mark the Ts with O to restore the original board
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'