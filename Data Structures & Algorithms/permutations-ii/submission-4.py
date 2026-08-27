class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        comb = []
        hashmap = {}
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)

        def dfs():
            if len(comb) == len(nums):
                res.append(comb.copy())
                return

            for key in hashmap:
                if hashmap[key] > 0:
                    comb.append(key)
                    hashmap[key] -= 1
                    dfs()
                    hashmap[key] += 1
                    comb.pop()

        dfs()
        return res