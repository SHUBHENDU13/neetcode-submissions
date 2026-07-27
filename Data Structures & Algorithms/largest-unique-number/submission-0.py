class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        freq_map = {}
        for n in nums:
            if n in freq_map:
                freq_map[n] += 1
            else:
                freq_map[n] = 1

        values = set()
        for num, freq in freq_map.items():
            if freq == 1:
                values.add(num)
        return max(values) if len(values) > 0 else -1
        