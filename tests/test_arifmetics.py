def test_arithmetic_and_logical_output(script_output):
    out = script_output("arifmetics.py")

    a, b = 5, 3
    expected = [
        str(a + b),        # 8
        str(a * b),        # 15
        str(a / b),        # 1.6666666666666667
        str(a**b),         # 125
        str(a // b),       # 1
        str(a % b),        # 2
        str(True and False),   # False
        str(True or False),    # True
        str(not True),         # False
        str(3 == "3"),         # False
        str([1, 2] == [1, 2]),         # True
        str([1, 2] is [1, 2]),         # False
    ]
    assert out == expected
