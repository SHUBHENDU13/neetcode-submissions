class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums

    def add(self, val: int) -> int:
        self.heap.append(val)
        self.heap.sort()
        return self.heap[len(self.heap) - self.k]
