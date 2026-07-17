def test_prints_hello_world(script_output):
    assert script_output("hello-world.py") == ["Hello World!"]
