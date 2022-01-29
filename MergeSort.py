from multiprocessing import set_forkserver_preload
from queue import Empty
from unittest import result


class LinkedStack:
    class _Node:
        __slots__ = "_element", "_next"

        def __init__(self, element, next=None) -> None:
            self._element = element
            self._next = next

    def __init__(self) -> None:
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def __iter__(self):
        top = self._head
        while top is not None:
            yield top._element
            top = top._next

    def _split(self, arr):
        slow = arr
        fast = arr._next
        while fast is not None:
            fast = fast._next
            if fast is not None:
                slow = slow._next
                fast = fast._next
        other = slow._next
        slow._next = None
        # print(arr._element, other._element)
        return [arr, other]

    def top(self):
        return self._head

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

    def MergeSort(self, arr=None):
        if arr is None or arr._next is None:
            return arr
        [L, R] = self._split(arr)
        # print(L._next._element, R._element)
        L = self.MergeSort(L)
        R = self.MergeSort(R)
        # self._head = self._mergeSorted(L, R)
        # print(x._element)
        return self._mergeSorted(L, R)

    def _mergeSorted(self, L, R):
        if R is None:
            return L
        if L is None:
            return R
        if L._element <= R._element:
            result = L
            result._next = self._mergeSorted(L._next, R)
        else:
            result = R
            result._next = self._mergeSorted(L, R._next)
        return result

    def show(self, x=None):
        while x is not None:
            print(x._element, end=" ")
            x = x._next


m = LinkedStack()
m.push(4)
m.push(39)
m.push(3)
m.push(23)

for i in m:
    print(i, end=" ")
print()
m.show(m.MergeSort(m.top()))

# for i in m:
#     print(i, end=" ")
