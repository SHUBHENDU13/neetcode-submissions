class Solution:
    def maxDifference(self, s: str) -> int:
        map = {}
        for c in s:
            map[c] = 1 + map.get(c, 0);

        maxOdd, minEven = float('-inf'), float('inf')
        for key in map:
            if map[key] % 2 == 0:
                minEven = min(minEven, map[key])
            else:
                maxOdd = max(maxOdd, map[key])

        return maxOdd - minEven