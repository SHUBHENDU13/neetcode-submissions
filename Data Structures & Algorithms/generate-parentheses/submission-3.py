class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        comb = []
        openN, closeN = 0, 0

        def dfs(openN, closeN):
            if openN == closeN == n:
                res.append(''.join(comb))
                return

            if openN < n:
                comb.append('(')
                dfs(openN + 1, closeN)
                comb.pop()

            if closeN < openN:
                comb.append(')')
                dfs(openN, closeN + 1)
                comb.pop()

        dfs(0, 0)
        return res