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
            return 1 + max(self.depth(c) for c in self.children(p))
