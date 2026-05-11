from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for i in points:
            d = -(i[0]**2 + i[1]**2)
            temp = [d, i]
            distances.append(temp)
        
        heapq.heapify(distances)
        resSet = []
        for i in range(k):
            resSet.append(distances.pop()[1])

        return resSet
