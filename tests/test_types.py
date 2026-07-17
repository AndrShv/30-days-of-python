def test_type_output(script_output):
    out = script_output("types.py")
    assert out == [
        str(type(10)),
        str(type(3.14)),
        str(type("Java to Python")),
        str(type(True)),
        str(type([1, 2, 3])),
        str(type(("a", "b", "c"))),
        str(type({"name": "John", "age": 30, "plan": "Learn Python"})),
    ]
