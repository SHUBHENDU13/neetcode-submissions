class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        if k > len(blocks):
            return -1
        l, r = 0, 0
        colormap = {'W' : 0, 'B' : 0}
        ans = float('inf')
        while r < len(blocks):
            colormap[blocks[r]] += 1
            if (r - l + 1) == k:
                ans = min(ans, colormap['W'])
                colormap[blocks[l]] -= 1
                l += 1
            r += 1
        return ans

