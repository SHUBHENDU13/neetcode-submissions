class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted_count = [0] * (n + 1)
        for j1, j2 in trust:
            trusted_count[j1] -= 1
            trusted_count[j2] += 1
        
        for i in range(1, len(trusted_count)):
            if trusted_count[i] == n - 1:
                return i
        return -1