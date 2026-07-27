class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        freq_map = {}
        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1
        
        values = set()
        for num, freq in freq_map.items():
            if freq == 1:
                values.add(num)

        return max(values) if values else -1