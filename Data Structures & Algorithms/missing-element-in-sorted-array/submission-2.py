class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        l,r = 0, len(nums)-1

        while l < r:
            mid = (l + r + 1)//2
            missing = nums[mid] - nums[0] - mid
            if missing < k:
                l = mid
            else:
                r = mid - 1
        
        return nums[0] + k + l