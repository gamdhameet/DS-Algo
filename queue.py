from collections import deque
q = deque()
q.appendleft(5)
q.appendleft(8)
q.appendleft(10)
q.pop()
q.pop()

from collections import deque


class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)