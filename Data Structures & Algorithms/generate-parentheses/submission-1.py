class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        comb = []

        def dfs(opencount, closecount):
            if opencount == closecount == n:
                res.append(''.join(comb))
                return

            if opencount < n:
                comb.append('(')
                dfs(opencount + 1, closecount)
                comb.pop()

            if closecount < opencount:
                comb.append(')')
                dfs(opencount, closecount + 1)
                comb.pop()

        dfs(0, 0)
        return res


            

            