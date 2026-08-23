class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        target = total//k
        if total % k != 0:
            return False

        nums.sort(reverse=True)
        # create k buckets
        res = [0] * k

        def backtrack(i):
            # if we reach end of nums, means we were successfully 
            # able to add every element in some bucket
            if i == len(nums):
                return True

            # j iterates over all the available buckets and we try 
            # to add nums[i] to some possible bucket
            for j in range(k):
                if res[j] + nums[i] <= target:
                    res[j] += nums[i]
                    if backtrack(i+1):
                        return True
                    res[j] -= nums[i]
                # if res[j] bucket was 0 and we failed to add nums[i] to that bucket, 
                # it'll fail for all other buckets as well so 
                # we will prune it to counter time limit exceed
                if res[j] == 0:
                    break
            return False
        return backtrack(0)
