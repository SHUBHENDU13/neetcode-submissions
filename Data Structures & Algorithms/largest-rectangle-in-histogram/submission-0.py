class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i, h in enumerate(heights):
            startInd = i
            while len(stack) > 0 and stack[-1][1] > h:
                stackInd, stackH = stack.pop()
                maxArea = max(maxArea, stackH * (i - stackInd))
                startInd = stackInd
            stack.append([startInd, h])

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea
