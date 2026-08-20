class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            if i >= len(nums) or total > target:
                return

            # keep including nums[i] in possible result
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            # never include nums[i] again in possible result
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res