class Node:
    def __init__(self, val, prev = None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        newNode, prev, next = Node(value), self.tail.prev, self.tail
        newNode.next = next
        newNode.prev = prev
        prev.next = newNode
        next.prev = newNode

    def appendleft(self, value: int) -> None:
        newNode, prev, next = Node(value), self.head, self.head.next
        newNode.next = next
        newNode.prev = prev
        prev.next = newNode
        next.prev = newNode

    def pop(self) -> int:
        if self.head.next == self.tail:
            return -1
        curr = self.tail.prev
        prev, next = curr.prev, curr.next
        prev.next = next
        next.prev = prev
        return curr.val

    def popleft(self) -> int:
        if self.head.next == self.tail:
            return -1
        curr = self.head.next
        prev, next = curr.prev, curr.next
        prev.next = next
        next.prev = prev
        return curr.val
        
        
