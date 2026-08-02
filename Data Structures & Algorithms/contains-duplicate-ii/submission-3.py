class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for l in range(len(nums)):
            for r in range(l+1, min(len(nums), l + k + 1)):
                if nums[l] == nums[r]:
                    return True
        return False