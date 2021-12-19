from test_utils import *
import random


def test_large():
    min_test(random.randint(10000, 30000), 0, 1000)
    max_test(random.randint(10000, 30000), 0, 1000)
    sum_test(random.randint(10000, 30000), 0, 1000)
    mul_test(random.randint(10000, 30000), 0, 1000)
