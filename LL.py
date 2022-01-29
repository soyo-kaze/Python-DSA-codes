from typing import AnyStr, Container


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
        newest = self._Node(e,  successor, predecessor)
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


class PositionalList(_DobuleLinkedBase):
    class Postion:
        def __init__(self, container, node) -> None:
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, __o: object) -> bool:
            return type(__o) is type(self) and __o._node is self._node

        def __ne__(self, __o: object) -> bool:
            return not (__o == self)

    def _validate(self, p):
        if not isinstance(p, self.Postion):
            raise TypeError("p must be proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._next is None:
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Postion(self, node)

    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def delete(self, p):
        original = self._validate(p)
        return self._delete_node(original)

    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)


def insertion_sort(L):
    if len(L) > 1:
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)
            value = pivot.element()
            if value > marker.element():
                marker = pivot
            else:
                walk = marker
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(marker)
                L.delete(pivot)
                L.add_before(walk, value)
