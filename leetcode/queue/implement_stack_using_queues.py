class MyStack:

    def __init__(self):
        self.queue = []
        
    def push(self, x: int) -> None:
        # O(1) usually, but since using a list it's O(n) running time
        self.queue.insert(0, x)
        
    def pop(self) -> int:
        # O(n) usually if using enqueue, O(n^2) using list insert
        for i in range(len(self.queue) - 1):
            val = self.queue.pop()
            self.queue.insert(0, val)
        return self.queue.pop()
        
    def top(self) -> int:
        # O(1) running time
        return self.queue[0]

    def empty(self) -> bool:
        # O(1) running time
        return True if len(self.queue) == 0 else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()