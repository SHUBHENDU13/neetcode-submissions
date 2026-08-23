class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        target = total//k
        if total % k != 0:
            return False

        nums.sort(reverse=True)
        res = [0] * k

        def backtrack(i):
            if i == len(nums):
                return True

            for j in range(k):
                if res[j] + nums[i] <= target:
                    res[j] += nums[i]
                    if backtrack(i+1):
                        return True
                    res[j] -= nums[i]
                if res[j] == 0:
                    break
            return False
        return backtrack(0)
