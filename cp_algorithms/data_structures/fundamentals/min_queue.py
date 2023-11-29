from itertools import accumulate


class ExtremaStack:
    def __init__(self, nums, func):
        self._func = func
        self._s1 = list(zip(nums, accumulate(nums, func)))
        self._s2 = []

    def extrema(self):
        if self._s1 and self._s2:
            return self._func(self._s1[-1][1], self._s2[-1][1])
        return self._s1[-1][1] if self._s1 else self._s2[-1][1]

    def append(self, num):
        extrema = self._func(num, self._s1[-1][1]) if self._s1 else num
        self._s1.append((num, extrema))

    def pop(self):
        if not self._s2:
            while self._s1:
                num, _ = self._s1.pop()
                extrema = self._func(num, self._s2[-1][1]) if self._s2 else num
                self._s2.append((num, extrema))
        num, _ = self._s2.pop()
        return num
