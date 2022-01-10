class Empty(Exception):
    pass


class ArrayStack:
    def __init__(self) -> None:
        self._data = []

    def __len__(self):
        return len(self._data)

    def __str__(self) -> str:
        if self.is_empty():
            return "Stack is empty"
        return "{}".format(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()


# S = ArrayStack()

# print(S)
# S.push(2)
# print(S)
# S.push(3)
# S.push(4)
# print(S)
# print(S.pop())
# print(S)
# print(S.top())
# print(S)


def is_matched(expr):
    lefty = "({["
    right = ")}]"
    S = ArrayStack()
    for x in expr:
        if x in lefty:
            S.push(x)
        elif x in right:
            if S.is_empty():
                return False
            elif right.index(x) != lefty.index(S.pop()):
                return False
    return S.is_empty()


def Html_matched(raw):
    j = raw.find("<")
    S = ArrayStack()
    while j != -1:
        k = raw.find(">", j + 1)
        tag = raw[j + 1 : k]
        if tag[0] != "/":
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find("<", k + 1)
    return S.is_empty()
