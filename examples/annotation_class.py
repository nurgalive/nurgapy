import time

from nurgapy import tyme
from nurgapy import trackbar


@tyme
def my_pow(a: int, b: int):
    for _ in range(10000000):
        res = a**b
    return res


class CheckTimeit:
    """
    You can measure exection time of functions inside the class.
    """

    def __init__(self, iterations):
        self.iterations = iterations

    @tyme  # here the call for the time measurement
    def measure_this(self):
        for _ in range(self.iterations):
            time.sleep(0.3)


if __name__ == "__main__":
    ## testing tyme wrapper
    result = my_pow(10, 10)
    print("Result: ", result)  # takes ~3 seconds

    ## testing progressbar
    for i in trackbar(range(10)):
        time.sleep(0.5)

    test = CheckTimeit(10)
    test.measure_this()
