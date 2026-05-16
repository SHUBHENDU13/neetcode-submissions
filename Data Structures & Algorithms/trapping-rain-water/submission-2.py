class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        maxLeft, maxRight = height[0], height[n-1]
        l,r = 1, n-2
        res = 0

        while l <= r:
            if maxLeft <= maxRight:
                res += maxLeft - height[l] if maxLeft - height[l] > 0 else 0
                maxLeft = max(maxLeft, height[l])
                l += 1
            else:
                res += maxRight - height[r] if maxRight - height[r] > 0 else 0
                maxRight = max(maxRight, height[r])
                r -= 1
        return res