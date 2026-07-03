class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(nums, comb):
            if not nums:
                res.append(comb.copy())
                return

            used = set()

            for i in range(len(nums)):
                if nums[i] in used:
                    continue

                used.add(nums[i])
                comb.append(nums[i])
                dfs(nums[0:i] + nums[i+1:], comb)
                comb.pop()

        dfs(nums, [])
        return res