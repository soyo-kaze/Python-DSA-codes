from PriorityQ import *


class HeapPriorityQueue(PriorityQueueBase):
    def __init__(self) -> None:
        self._data = []

    def _parent(self, j):
        return (j-1)//2

    def _left(self, j):
        return 2*j + 1

    def _right(self, j):
        return 2*j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[left] > self._data[right]:
                    small_child = right
            if self._data[j] > self._data[small_child]:
                self._swap(small_child, j)
                self._downheap(small_child)

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data)-1)

    def min(self):
        return self._data[0]

    def remove_min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty')
        self._swap(0, len(self._data)-1)
        answer = self._data.pop()
        self._downheap(0)
        return (answer._key, answer._value)

    def __iter__(self):
        # print(self.is_empty())
        while not self.is_empty():
            yield self.remove_min()


x = HeapPriorityQueue()
x.add(2, 3)
x.add(4, 2)
x.add(32, 3)
x.add(1, 4)
x.add(3, 5)

# print(x.min())
# print(x.remove_min())
for i in x:
    print("key:{} value: {} ".format(i[0], i[1]))
