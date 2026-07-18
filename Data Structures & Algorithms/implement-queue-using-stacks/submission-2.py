class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.size = 0

    def push(self, x: int) -> None:
        # if not self.stack1:
        #     self.stack1.append(x)
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        self.size += 1

    def pop(self) -> int:
        if self.stack1:
            self.size -= 1
            return self.stack1.pop()

    def peek(self) -> int:
        if self.stack1:
            return self.stack1[len(self.stack1)-1]
        return -1

    def empty(self) -> bool:
        return False if self.size > 0 else True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()