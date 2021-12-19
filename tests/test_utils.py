import utils
import random


def min_test(length, num_a, num_b):
    for i in range(10):
        base = random.randint(num_a, num_b)
        nums = [base + x for x in range(length)]

        assert base == utils.min_num(nums)


def max_test(length, num_a, num_b):
    for i in range(10):
        base = random.randint(num_a, num_b)
        nums = [base - x for x in range(length)]

        assert base == utils.max_num(nums)


def sum_test(length, num_a, num_b):
    for i in range(10):
        nums = [random.randint(num_a, num_b) for x in range(length)]
        _sum = 0
        for j in nums:
            _sum += j

        assert _sum == utils.sum_nums(nums)


def mul_test(length, num_a, num_b):
    for i in range(10):
        nums = [random.randint(num_a, num_b) for x in range(length)]
        _mul = 1
        for j in nums:
            _mul *= j

        assert _mul == utils.mul_nums(nums)
