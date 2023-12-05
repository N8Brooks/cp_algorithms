from typing import List
from random import randrange
from ....cp_algorithms.data_structures.trees.fenwick_tree import (
    FenwickTree,
)


class MockFenwickTree:
    def __init__(self, nums: List[int]):
        self._nums = nums

    def update(self, i: int, delta: int):
        self._nums[i] += delta

    def query(self, i: int, j: int) -> int:
        return sum(self._nums[i : j + 1])


def test_add_fenwick_tree():
    for _ in range(1000):
        n = randrange(1, 1000)
        nums = [randrange(-1000, 1000) for _ in range(n)]
        mock = MockFenwickTree(nums)
        true = FenwickTree(nums)
        for _ in range(1000):
            if randrange(2):
                i = randrange(n)
                delta = randrange(-1000, 1000)
                mock.update(i, delta)
                true.update(i, delta)
            else:
                i = randrange(n)
                j = randrange(i, n)
                assert mock.query(i, j) == true.query(i, j)
