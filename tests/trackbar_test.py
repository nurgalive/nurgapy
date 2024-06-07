from nurgapy import trackbar


def test_trackbar(capsys):
    it = range(10)
    list(trackbar(it, prefix="Progress:", size=10))

    captured = capsys.readouterr()
    output_lines = captured.out.splitlines()

    # Check the initial output
    assert output_lines[0].startswith("0:00:00 Progress:[..........] 0/10")

    # Check intermediate steps
    for i in range(1, 10):
        bar_progress = "█" * i + "." * (10 - i)
        expected_line = f"0:00:00 Progress:[{bar_progress}] {i}/10"
        assert any(
            expected_line in line for line in output_lines
        ), f"Expected line not found: {expected_line}"

    # Check the final output
    assert output_lines[-1] == "", "Expected final line to be empty"
