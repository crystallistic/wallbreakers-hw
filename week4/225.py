class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._queue = collections.deque()
        self._top = None

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self._queue.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if not self.empty():
            for i in range(len(self._queue)-1):
                self._queue.append(self._queue.popleft())
        return self._queue.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        if not self.empty():
            for i in range(len(self._queue)-1):
                self._queue.append(self._queue.popleft())
        item = self._queue.popleft()
        self._queue.append(item)
        return item

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not len(self._queue)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()