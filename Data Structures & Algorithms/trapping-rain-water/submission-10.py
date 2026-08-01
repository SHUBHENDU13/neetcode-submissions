class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        maxl, maxr = height[0], height[-1]
        total = 0
        l, r = 0, len(height)-1
        while l < r:
            if maxl <= maxr:
                total += maxl - height[l] if (maxl - height[l]) >= 0 else 0
                l += 1
                maxl = max(maxl, height[l])
            else:
                total += maxr - height[r] if (maxr - height[r]) >= 0 else 0
                r -= 1
                maxr = max(maxr, height[r])
        return total