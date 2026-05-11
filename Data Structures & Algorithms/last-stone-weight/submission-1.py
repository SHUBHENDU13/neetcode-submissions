class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 1:
            stones.sort()
            s1 = stones.pop()
            s2 = stones.pop()
            if s1 > s2:
                stones.append(s1-s2)
            else:
                stones.append(s2-s1)
        return stones[0]