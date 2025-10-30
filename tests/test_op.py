from src.math_op import add, sub

def test_add():
    assert add(2,3) == 5
    assert add(-1, 1) == 0
    assert add(0,9) == 9

def test_sub():
    assert sub(1,2) == -1
    assert sub(2, 1) == 1
    assert sub(9,9) == 0
