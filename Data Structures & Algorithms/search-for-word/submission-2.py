class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        ROWS, COLS = len(board), len(board[0])
        visit = set()
        comb = []

        def backtrack(r, c, i):
            if len(comb) == len(word):
                if ''.join(comb) == word:
                    return True
                else:
                    return False

            if (r >= ROWS or c >= COLS or min(r, c) < 0
                or (r, c) in visit or board[r][c] != word[i]):
                return False

            comb.append(board[r][c])
            visit.add((r, c))
            for dr, dc in directions:
                if backtrack(r + dr, c + dc, i + 1):
                    return True
            comb.pop()
            visit.remove((r, c))
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0):
                    return True
        return False