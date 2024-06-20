from nurgapy import trackbar
from nurgapy.trackbar import chop_microseconds
from datetime import timedelta
from io import StringIO


def test_chop_microseconds():
    delta = timedelta(seconds=1, microseconds=123456)
    expected = timedelta(seconds=1)
    result = chop_microseconds(delta)
    assert result == expected

    delta = timedelta(days=1, seconds=1, microseconds=987654)
    expected = timedelta(days=1, seconds=1)
    result = chop_microseconds(delta)
    assert result == expected


def test_trackbar_basic_functionality():
    output = StringIO()
    items = list(range(10))
    processed_items = list(trackbar(items, prefix="Progress:", size=10, out=output))
    assert items == processed_items
    output_lines = output.getvalue().strip().split("\r")
    assert all("Progress:" in line for line in output_lines)
    assert all("[" in line and "]" in line for line in output_lines)
    assert len(output_lines) == len(items) + 1


def test_trackbar_output_format():
    output = StringIO()
    items = list(range(5))
    list(trackbar(items, prefix="Test:", size=5, out=output))
    output_lines = output.getvalue().strip().split("\r")
    assert "Test:[.....]" in output_lines[0]
    assert "Test:[█████]" in output_lines[-1]


def test_trackbar_correct_progress():
    output = StringIO()
    items = list(range(4))
    list(trackbar(items, prefix="Progress:", size=8, out=output))
    output_lines = output.getvalue().strip().split("\r")

    expected_progress_states = [
        "Progress:[........]",
        "Progress:[██......]",
        "Progress:[████....]",
        "Progress:[██████..]",
        "Progress:[████████]",
    ]

    for expected, actual in zip(expected_progress_states, output_lines):
        assert expected in actual
