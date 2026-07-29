class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
        curr = nums[0]
        for i in range(len(nums)-1):
            next_ele = nums[i+1]
            if curr + 1 == next_ele:
                curr = next_ele
                continue
            else:
                while k > 0 and curr + 1 != next_ele:
                    curr += 1
                    k -= 1
                if k == 0: return curr
                curr = next_ele
        return curr + k