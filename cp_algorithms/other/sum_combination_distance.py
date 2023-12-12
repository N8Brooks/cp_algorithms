def sum_combination_distance(nums: list[int]):
    i = 1 - len(nums)
    ans = 0
    for num in sorted(nums):
        ans += i * num
        i += 2
    return ans
