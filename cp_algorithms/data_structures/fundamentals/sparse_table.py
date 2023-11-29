from abc import ABC, abstractmethod
from itertools import accumulate, islice
from typing import List, Callable


class SparseTable(ABC):
    def __init__(self, nums: List[int], func: Callable[[int, int], int]):
        self._func = func
        n = len(nums)
        self._data = list(
            accumulate(
                range(n.bit_length() - 1),
                lambda row, i: list(map(func, row, islice(row, (1 << i), None))),
                initial=nums,
            )
        )

    @classmethod
    @abstractmethod
    def query(cls, left: int, right: int) -> int:
        pass


class AddSparseTable(SparseTable):
    """Defines a generic $O(log(n))$ query operation across a range"""

    def __init__(self, nums: List[int], func: Callable[[int, int], int], identity: int):
        self._identity = identity
        super().__init__(nums, func)

    def query(self, left: int, right: int) -> int:
        k = len(self._data)
        res = self._identity
        for i, row in zip(reversed(range(k)), reversed(self._data)):
            if (1 << i) <= right - left + 1:
                res = self._func(res, row[left])
                left += 1 << i
        return res


class MinMaxSparseTable(SparseTable):
    """
    Defines a specialized $O(1)$ query operation across a range.
    This should be used when it doesn't matter if a a value is processed multiple times, like `min`, `max`, or `or_`.
    """

    def __init__(self, nums: List[int], func: Callable[[int, int], int]):
        super().__init__(nums, func)

    def query(self, left: int, right: int) -> int:
        i = (right - left + 1).bit_length() - 1
        return self._func(
            self._data[i][left],
            self._data[i][right - (1 << i) + 1],
        )
