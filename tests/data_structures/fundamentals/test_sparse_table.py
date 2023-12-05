from functools import reduce
from operator import add
from typing import Callable, List
from random import randrange
from ....cp_algorithms.data_structures.fundamentals.sparse_table import (
    MinMaxSparseTable,
    AddSparseTable,
)
import sys


class MockSparseTable:
    def __init__(self, nums: List[int], func: Callable[[int, int], int], identity: int):
        self._nums = nums
        self._func = func
        self._identity = identity

    def query(self, left: int, right: int) -> int:
        return reduce(self._func, self._nums[left : right + 1], self._identity)


def test_add_sparse_table():
    for _ in range(100):
        n = randrange(1, 1000)
        nums = [randrange(-1000, 1000) for _ in range(n)]
        mock = MockSparseTable(nums, add, 0)
        true = AddSparseTable(nums, add, 0)
        for _ in range(100):
            left = randrange(n)
            right = randrange(left, n)
            assert mock.query(left, right) == true.query(left, right)


def test_min_sparse_table():
    for _ in range(100):
        n = randrange(1, 1000)
        nums = [randrange(-1000, 1000) for _ in range(n)]
        mock = MockSparseTable(nums, min, sys.maxsize)
        true = MinMaxSparseTable(nums, min)
        for _ in range(100):
            left = randrange(n)
            right = randrange(left, n)
            assert mock.query(left, right) == true.query(left, right)


def test_max_sparse_table():
    for _ in range(100):
        n = randrange(1, 1000)
        nums = [randrange(-1000, 1000) for _ in range(n)]
        mock = MockSparseTable(nums, max, -sys.maxsize)
        true = MinMaxSparseTable(nums, max)
        for _ in range(100):
            left = randrange(n)
            right = randrange(left, n)
            assert mock.query(left, right) == true.query(left, right)
