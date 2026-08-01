class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights:
            return 0
        maxL, maxR = [0] * len(heights), [0] * len(heights)
        water_trapped = [0] * len(heights)

        maxL[0] = heights[0]
        for i in range(1, len(heights)):
            maxL[i] = max(maxL[i-1], heights[i])

        maxR[-1] = heights[-1]
        for j in range(len(heights)-2, -1, -1):
            maxR[j] = max(maxR[j+1], heights[j])
            
        for i in range(len(water_trapped)):
            water_trapped[i] = min(maxL[i], maxR[i]) - heights[i]

        return sum(water_trapped)