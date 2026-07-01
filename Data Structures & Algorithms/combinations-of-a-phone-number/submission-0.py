class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i, comb):
            if i == len(digits) and comb:
                res.append(comb)
                return

            if i >= len(digits):
                return

            for c in digitToChar[digits[i]]:
                comb = comb + c
                dfs(i+1, comb)
                comb = comb[:-1]

        dfs(0, '')
        return res

