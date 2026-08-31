class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}
        
        def dp(i, j):
            if (i,j) in cache:
                return cache[(i,j)]

            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            
            if word1[i] == word2[j]:
                return dp(i + 1, j + 1)
            else:
                insert = 1 + dp(i, j + 1)
                delete = 1 + dp(i + 1, j)
                replace = 1 + dp(i + 1, j + 1)
                cache[(i,j)] = min(insert, delete, replace)
                return cache[(i,j)]

        return dp(0,0)