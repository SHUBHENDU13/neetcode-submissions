class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []
        self.helper(1, [], combs, n, k)
        return combs

    def helper(self, i, currCombs, combs, n, k):
        if len(currCombs) >= k:
            combs.append(currCombs.copy())
            return

        if i > n:
            return

        currCombs.append(i)
        self.helper(i+1, currCombs, combs, n, k)
        currCombs.pop()

        self.helper(i+1, currCombs, combs, n, k)