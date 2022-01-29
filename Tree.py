class NotImplementedError(Exception):
    pass


class Tree:
    """abstract base class representing a tree structure"""

    class Positon:
        """nested position class used for determining the position of the node."""

        def element(self):
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, __o: object) -> bool:
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, __o: object) -> bool:
            return not (self == __o)

    # --------- abstract methods to be implemented by the subclass -------------

    def root(self):
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        raise NotImplementedError('must be implemented by subclass')

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def height(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self.height(c) for c in self.children(p))


class BinaryTree(Tree):
    def __init__(self) -> None:
        super().__init__()

    def left(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            return self.left(parent)

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)


class LinkedBinaryTree(BinaryTree):
    class _Node:
        def __init__(self, element, parent=None, left=None, right=None) -> None:
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Postion:
        def __init__(self, container, node) -> None:
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, __o: object) -> bool:
            return type(__o) is type(self) and __o._node is self._node

    def _validate(self, p):
        if not isinstance(p, self.Postion):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is not longer valid')
        return p._node

    def _make_position(self, node):
        return self.Postion(self, node) if node is not None else None

    def __init__(self) -> None:
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        for p in self.positions():
            yield p.element()

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def _add_root(self, e):
        if self._root is not None:
            raise ValueError('Root Exists')
        self._size += 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)

    def _add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('Right child exists')
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._left)

    def _replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        node = self._validate(p)

    def preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def position(self):
        for p in self.preorder():
            yield p
