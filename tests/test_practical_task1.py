def test_prints_circle_area(script_output):
    out = script_output("practical-task1.py")
    assert out == ["2826.0"]
    # radius = 30, area = 3.14 * 30 ** 2
    assert float(out[0]) == 3.14 * 30**2
