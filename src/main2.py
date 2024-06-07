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
