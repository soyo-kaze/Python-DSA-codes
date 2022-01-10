import ctypes
from typing import ChainMap


class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError("invalid index")
        return self._A[k]

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _make_array(self, c):
        return (c * ctypes.py_object)()


# c = DynamicArray()

# c.append(2)
# c.append(3)
# c._resize(4)
# for i in c:
#     print(i)


class GameEntry:
    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return "({0}, {1})".format(self._name, self._score)


class Scoreboard:
    def __init__(self, capacity) -> None:
        self._board = [None] * capacity
        self._n = 0

    def __getitem__(self, k):
        if self._n == 0:
            raise IndexError("invalid index!!")
        return self._board[k]

    def __str__(self):
        return "\n".join(str(self._board[i]) for i in range(self._n))

    def add(self, entry):
        score = entry.get_score()
        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):
                self._n += 1
            j = self._n - 1
            while j > 0 and self._board[j - 1].get_score() < score:
                self._board[j] = self._board[j - 1]
                j -= 1
            self._board[j] = entry


# Board = Scoreboard(4)

# for i in [["sameer", 2312], ["sam", 2133], ["gam", 4533], ["Ram", 22300]]:
#     Board.add(GameEntry(i[0], i[1]))
# c = Board
# print(c)


def insertionSort(arr):
    n = len(arr) - 1
    for i in range(1, n):
        now = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > now:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = now
    return arr


# print(insertionSort([5, 2, 2, 1, 3, 6, 8, 3, 10]))
