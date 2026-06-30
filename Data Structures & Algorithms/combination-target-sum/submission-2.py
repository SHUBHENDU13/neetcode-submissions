class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            if i >= len(nums) or total > target:
                return

            # include current element
            cur.append(nums[i])
            total += nums[i]
            dfs(i, cur, total)
            
            # cleanup of cur and total
            cur.pop()
            total -= nums[i]

            # not include current element
            dfs(i+1, cur, total)

        dfs(0, [], 0)
        return res
