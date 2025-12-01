from core_python.project1.file1 import greet


def test_greet():
    assert greet("Alice") == "Hello, Alice from project1!"
