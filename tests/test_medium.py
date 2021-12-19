from test_utils import *
import random


def test_common():
    min_test(random.randint(100, 300), 0, 1000)
    max_test(random.randint(100, 300), 0, 1000)
    sum_test(random.randint(100, 300), 1, 1000)
    mul_test(random.randint(100, 300), 1, 1000)
