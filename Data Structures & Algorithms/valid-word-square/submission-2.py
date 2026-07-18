class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        colword = []
        rows = len(words)
        cols = 0
        for word in words:
            cols = max(cols, len(word))

        if cols != len(words) or cols != rows:
            return False

        for col in range(cols):
            newword = []
            for row in range(rows):
                if col < len(words[row]):
                    newword.append(words[row][col])

            newword = ''.join(newword)
            colword.append(newword)

        return words == colword