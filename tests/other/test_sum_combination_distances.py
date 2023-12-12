from itertools import combinations
from random import randint

from ...cp_algorithms.other.sum_combination_distance import sum_combination_distance


def sum_combination_distance_2(nums: list[int]):
    return sum(b - a for a, b in combinations(sorted(nums), 2))


def test_sum_combination_distances():
    for _ in range(100):
        nums = [randint(-100, 100) for _ in range(randint(1, 100))]
        assert sum_combination_distance(nums) == sum_combination_distance_2(nums)
