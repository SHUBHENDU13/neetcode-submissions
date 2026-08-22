class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visit = set()
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r >= len(board) or c >= len(board[0]) or min(r, c) < 0
                or (r, c) in visit or board[r][c] != word[i]):
                return False
            visit.add((r, c))
            for dr, dc in directions:
                if dfs(r + dr, c + dc, i + 1):
                    return True
            visit.remove((r, c))
            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True
        return False


            