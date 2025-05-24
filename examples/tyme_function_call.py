"""
This example shows how to use the `tyme` from the `nurgapy` library.
It demonstrates measuring execution time of a function without using the annotation.
"""

import time
from nurgapy import tyme


def sleep_func(n):
    time.sleep(n)
    return n


def test_tyme():
    result = tyme(sleep_func)
    res = result(1)
    print(res)


test_tyme()
