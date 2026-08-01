class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol = 0
        l, r = 0, len(heights)-1
        while l < r:
            local_vol = min(heights[l], heights[r]) * (r - l)
            max_vol = max(max_vol, local_vol)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return max_vol