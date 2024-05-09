import time

from nurgapy import tyme
from nurgapy import trackbar


@tyme
def my_pow(a: int, b: int):
    for _ in range(10000000):
        res = a**b
    return res


class CheckTimeit:
    def __init__(self, iterations):
        self.iterations = iterations

    @tyme
    def measure_this(self):
        for _ in range(self.iterations):
            time.sleep(0.3)


if __name__ == "__main__":
    ## testing timeit wrapper
    result = my_pow(10, 10)
    # print("Execution time: ", exec_time) # prints after 0.07347989082336426 seconds
    print("Result: ", result)  # takes ~3 seconds

    ## testing progressbar
    for i in trackbar(range(10)):
        time.sleep(0.5)

    test = CheckTimeit(10)
    test.measure_this()
