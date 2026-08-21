class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(opencount, closecount, comb):
            if opencount == closecount == n:
                res.append(''.join(comb))
                return

            if opencount < n:
                comb.append('(')
                dfs(opencount + 1, closecount, comb)
                comb.pop()

            if closecount < opencount:
                comb.append(')')
                dfs(opencount, closecount + 1, comb)
                comb.pop()

        dfs(0, 0, [])
        return res


            

            