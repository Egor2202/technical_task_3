def min_num(nums):
    a = nums[0]
    for num in nums:
        if num < a:
            a = num
    return a


def max_num(nums):
    a = nums[0]
    for num in nums:
        if num > a:
            a = num
    return a


def sum_nums(nums):
    res = 0
    for i in nums:
        res += i
    return res


def mul_nums(nums):
    res = 1
    for i in nums:
        res *= i
    return res
