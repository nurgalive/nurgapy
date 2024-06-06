from nurgapy import tyme
import time


def sleep_func(n):
    """
    Function used for testing.
    """
    time.sleep(n)
    return n


# Asserting the function output
# https://docs.pytest.org/en/stable/how-to/capture-stdout-stderr.html#accessing-captured-output-from-a-test-function
def test_tyme(capsys):
    """
    Tests the tyme function output.
    """
    result = tyme(sleep_func)
    result(1)

    captured = capsys.readouterr()
    assert captured.out == "Function sleep_func(1,) Took 1.0 seconds\n"
