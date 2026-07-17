class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        m, n = len(word), len(abbr)

        while i < m and j < n:
            if abbr[j] == '0':
                return False

            if word[i] == abbr[j]:
                i, j = i + 1, j + 1
            else:
                if abbr[j].isalpha():
                    return False
                else:
                    count = 0
                    while j < n and abbr[j].isdigit():
                        count = 10 * count + int(abbr[j])
                        j += 1
                    i += count

        return i == m and j == n