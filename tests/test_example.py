# tests/test_example.py

def test_the_truth(): # A test function that does nothing
    pass


def test_two_plus_two_fail():
    assert 2 + 2 == 5

def test_two_plus_two_pass():
    assert 2 + 2 == 4
