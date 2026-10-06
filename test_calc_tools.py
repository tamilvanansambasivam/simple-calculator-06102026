from calc_tools import add, subtract, multiply, divide, calculate


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero_returns_none():
    assert divide(10, 0) is None


def test_calculate_each_operator():
    assert calculate(6, "+", 2) == 8
    assert calculate(6, "-", 2) == 4
    assert calculate(6, "*", 2) == 12
    assert calculate(6, "/", 2) == 3


def test_calculate_unknown_operator():
    assert calculate(6, "%", 2) is None


def test_calculate_divide_by_zero():
    assert calculate(6, "/", 0) is None