class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        n = len(words)
        colword = []
        for c in range(n):
            curword = []
            r = 0
            while r < n and c < len(words[r]):
                curword.append(words[r][c])
                r += 1
            curword = ''.join(curword)
            colword.append(curword)

        for i in range(len(words)):
            if colword[i] != words[i]:
                return False
        return True