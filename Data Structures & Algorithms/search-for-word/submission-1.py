class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visit = set()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (r >= ROWS or c >= COLS or min(r, c) < 0
                or (r, c) in visit or board[r][c] != word[i]):
                return False

            visit.add((r, c))
            for dr, dc in directions:
                if dfs(r + dr, c + dc, i + 1):
                    return True
            
            visit.remove((r, c))
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
            
