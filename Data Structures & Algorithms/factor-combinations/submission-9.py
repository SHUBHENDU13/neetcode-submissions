class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        ans = []
        self.backtrack([n], ans)
        return ans

    def backtrack(self, factors, ans):
        if len(factors) > 1:
            ans.append(factors.copy())

        last_factor = factors.pop()

        i = 2 if not factors else factors[-1]

        while i <= last_factor//i:
            if last_factor % i == 0:
                factors.append(i)
                factors.append(last_factor//i)
                self.backtrack(factors, ans)
                factors.pop()
                factors.pop()
            i += 1
        
        factors.append(last_factor)


