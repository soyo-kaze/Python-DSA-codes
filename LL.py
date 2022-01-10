from typing import AnyStr


class Empty(Exception):
    pass


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

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer


print()


class LinkedQueue:
    class _Node:
        __slots__ = "_element", "_next"

        def __init__(self, element, next=None) -> None:
            self._element = element
            self._next = next

    def __init__(self) -> None:
        self._head = None
        self._size = 0
        self._tail = None

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, e):
        newest = self._Node(e)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1


class _DobuleLinkedBase:
    class _Node:
        def __init__(self, element=None, next=None, prev=None) -> None:
            self._element = element
            self._next = next
            self._prev = prev

    def __init__(self) -> None:
        self._header = self._Node()
        self._trailer = self._Node()
        self._trailer._prev = self._header
        self._header._next = self._trailer
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, e):
        predecessor = e._prev
        successor = e._next
        predecessor._next = successor
        successor._prev = predecessor
        element = e._element
        e._prev = e._next = e._element = None
        self._size -= 1
        return element
