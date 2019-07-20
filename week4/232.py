class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._stack = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self._stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.empty():
            for _ in range(len(self._stack)-1):
                self._stack.appendleft(self._stack.pop())
        return self._stack.pop()
                

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.empty():
            for _ in range(len(self._stack)-1):
                self._stack.appendleft(self._stack.pop())
        item = self._stack.pop()
        self._stack.appendleft(item)
        return item 
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not len(self._stack)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()