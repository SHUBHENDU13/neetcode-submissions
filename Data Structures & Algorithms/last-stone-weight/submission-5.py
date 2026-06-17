class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            # we are maintaining -ve values, so when popping from minHeap, 
            # always first < second, so when we add (first - second) it automatically 
            # adds the -ve value for the difference
            # and we don't care for first == second case
            if second > first:
                heapq.heappush(stones, first - second) 
        # below taking care if all weights are destroyed, so we might get listIndexOutOfRange error
        stones.append(0)
        return abs(stones[0])
