from hello import greet

def test_greet_with_name():
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") == "Hello, Bob!"

def test_greet_empty_name():
    assert greet("") == "Hello, World!"
