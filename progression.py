class Progression:
    def __init__(self, start=0) -> None:
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self) -> int:
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self) -> object:
        return self

    def print_progression(self, n: int) -> None:
        print(' '.join(str(next(self)) for j in range(n)))


p = Progression(1)
p.print_progression(20)


class ArithmeticProgression(Progression):
    def __init__(self, step, start=None) -> None:
        self._step = step
        if start is None:
            self._step, start = 1, step
        super().__init__(start)

    def _advance(self) -> None:
        self._current += self._step


ap = ArithmeticProgression(2)
ap.print_progression(10)
ap2 = ArithmeticProgression(2, 1)
ap2.print_progression(10)


class GeometricProgression(Progression):
    def __init__(self, base=2, start=1) -> None:
        self._base = base
        super().__init__(start)

    def _advance(self):
        self._current *= self._base


gp = GeometricProgression()
gp.print_progression(10)


class FibonacciProgression(Progression):
    def __init__(self, first=0, second=1) -> None:
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        self._prev, self._current = self._current, self._current + self._prev


fp = FibonacciProgression()
fp.print_progression(10)

