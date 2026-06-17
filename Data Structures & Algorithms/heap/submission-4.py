class MinHeap:
    
    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:
        self.heap.append(val)
        self.bubble_up(len(self.heap)-1)

    def pop(self) -> int:
        if len(self.heap) <= 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()
        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.bubble_down(1)
        return res

    def top(self) -> int:
        return self.heap[1] if len(self.heap) > 1 else -1

    def heapify(self, nums: List[int]) -> None:
        self.heap = [0] + nums
        for i in range(len(nums) // 2, 0, -1):
            self.bubble_down(i)

    def bubble_up(self, index):
        parent = index//2
        while parent > 0 and self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            parent = index//2
        
    def bubble_down(self, index):
        child = index * 2
        while child < len(self.heap):
            if (child+1 < len(self.heap) and self.heap[child] > self.heap[child+1]):
                child += 1
            if (self.heap[index] <= self.heap[child]):
                break
            self.heap[child], self.heap[index] = self.heap[index], self.heap[child]
            index = child
            child = 2 * index
