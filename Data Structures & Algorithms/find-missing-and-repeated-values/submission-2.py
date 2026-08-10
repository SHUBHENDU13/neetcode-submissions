class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid) * len(grid)
        hashmap = {i:0 for i in range(1, n+1)}
        for r in range(len(grid)):
            for c in range(len(grid)):
                hashmap[grid[r][c]] += 1
        repeat, missing = 0, 0
        for key in hashmap:
            if hashmap[key] > 1:
                repeat = key
            if hashmap[key] == 0:
                missing = key
        return [repeat, missing]