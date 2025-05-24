"""
This example shows how to use the `tyme` decorator and `trackbar` from the `nurgapy` library.
It demonstrates measuring execution time of a function and displaying a progress bar for iterations.
"""

import time

from nurgapy import tyme
from nurgapy import trackbar


@tyme
def my_pow(a: int, b: int):
    """Here is an example how to the `tyme` decorator to measure execution time of a function."""
    res = None
    for _ in range(10000000):
        res = a**b
    return res


class CheckTimeit:
    """You can measure execution time of functions inside the class."""

    def __init__(self, iterations):
        self.iterations = iterations

    @tyme  # here the call for the tyme to measure execution time inside the class
    def measure_this(self):
        for _ in range(self.iterations):
            time.sleep(0.2)


if __name__ == "__main__":
    print("====== Showing the tyme wrapper ====")
    # testing the tyme wrapper
    result = my_pow(10, 10)
    print("Result: ", result)  # takes ~3 seconds

    print("====== Showing the tyme wrapper for the method inside the class ====")
    check_time_inside_this_class = CheckTimeit(10)
    check_time_inside_this_class.measure_this()

    print("====== Showing the trackbar ====")
    # testing the progressbar
    for i in trackbar(range(10)):
        if i % 3 == 0:
            print(f"almost ready, {i}")  # you can print() inside the trackbar
        time.sleep(2)
