from typing import List


# All fenwick trees implemented with 0-based indexing


class FenwickTree:
    def __init__(self, nums: List[int]):
        self._n = len(nums)
        self._bit = [0] * self._n
        for i, num in enumerate(nums):
            self._bit[i] += num
            j = i | (i + 1)
            if j < self._n:
                self._bit[j] += self._bit[i]

    def update(self, i: int, delta: int) -> None:
        while i < self._n:
            self._bit[i] += delta
            i |= i + 1

    def query(self, i: int, j: int) -> int:
        return self.queryRight(j) - self.queryRight(i - 1)

    def queryRight(self, j: int) -> int:
        res = 0
        while j >= 0:
            res += self._bit[j]
            j = (j & (j + 1)) - 1
        return res
