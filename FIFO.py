class Empty(Exception):
    pass


class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, c):
        old = self._data
        self._data = [None] * c
        walk = self._front
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]

    def __str__(self) -> str:
        return "{}".format(self._data)


Q = ArrayQueue()
Q.enqueue(3)
Q.enqueue(4)
print(Q)
print(Q.dequeue())
print(Q)


"""
Deque Methods that it supports:
- add_first(e)
- add_last(e)
- delete_first()
- delete_last()
- first()
- last()
- is_empty()
- len(D)

"""


class Deque:
    DEFAULT_CAPACITY = 10

    def __init__(self) -> None:
        self._data = [None] * Deque.DEFAULT_CAPACITY
        self._front = 0
        self._size = 0
        self.back = (self._front + self._size - 1) % len(self._data)

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _resize(self, c):
        old = self._data
        self._data = [None] * c
        walk = self._front
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

    def add_first(self, e):
        if len(self._data) == self._size:
            self._resize(2 * len(self._data))
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1

    def add_last(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def delete_first(self):
        if self.is_empty():
            raise Empty("deque is empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def delete_last(self):
        if self.is_empty():
            raise Empty("deque is empty")
        answer = self._data[self.back]
        self._data[self.back] = None
        self.back = (self.back - 1) % len(self._data)
        self._size -= 1
        return answer
