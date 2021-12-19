from test_utils import *
import random


def test_large():
    min_test(random.randint(10000, 30000), 2 ** 15, 2 ** 30)
    max_test(random.randint(10000, 30000), 2 ** 15, 2 ** 30)
    sum_test(random.randint(10000, 30000), 2 ** 15, 2 ** 30)
    mul_test(random.randint(10000, 30000), 2 ** 15, 2 ** 30)
