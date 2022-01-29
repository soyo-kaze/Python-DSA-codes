def BinInorder(p):
    if x := p._left is not None:
        BinInorder(x)
    yield p._element
    if x := p._right is not None:
        BinInorder(x)


x = [[3, 4], [[2, 3], 4]]


def some(x):
    # print("hello")
    yield [x, "x"]
    if not isinstance(x, int):
        for c in x:
            for o in some(c):
                # print(o)
                yield [o, "o"]
    # print(x)


def gg(x):
    for i in some(x):
        print("invoked", i)
        yield i


for i in gg(x):
    pass
