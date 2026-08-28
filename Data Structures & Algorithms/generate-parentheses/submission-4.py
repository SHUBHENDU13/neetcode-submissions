class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        comb = []
        openN = closeN = 0

        def backtrack():
            nonlocal openN
            nonlocal closeN
            if openN == closeN == n:
                res.append(''.join(comb))
                return

            if openN < n:
                comb.append('(')
                openN += 1
                backtrack()
                comb.pop()
                openN -= 1

            if closeN < openN:
                comb.append(')')
                closeN += 1
                backtrack()
                comb.pop()
                closeN -= 1

        backtrack()
        return res