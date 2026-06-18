class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for i in range(len(points)):
            distance = (points[i][0]**2 + points[i][1]**2)
            minHeap.append([distance, points[i]])

        heapq.heapify(minHeap)
        resSet = []
        for i in range(k):
            tmp = heapq.heappop(minHeap)
            resSet.append(tmp[1])

        return resSet