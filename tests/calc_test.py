import sys
sys.path.append("/Users/lindaoranya/PycharmProjects/pypi_calculator/src")
import pytest
from pytest import ExitCode
from calculator import Calculator

calc = Calculator()


def test_add():
    assert calc.add(10) == 10


def test_subtract():
    assert calc.subtract(2) == 8


def test_divide():
    assert calc.divide(2) == 4


def test_memory_val():
    assert calc.memory_val == 4


def test_multiply():
    assert calc.multiply(0) == 0


def test_zero_division():
    assert calc.subtract(20) == -20
    assert calc.add(-10) == -30
    assert calc.divide(0) == None
    assert calc.memory_val == -30


def test_modulus():
    assert calc.modulus(3) == 0
    assert calc.memory_val == 0


def test_root():
    my_cal = Calculator()
    assert my_cal.add(16) == 16
    assert my_cal.square_root(2) == 4
    with pytest.raises(Exception):
        Calculator().square_root(2)


def test_reset():
    calc.reset()
    assert calc.memory_val == 0



def test_zero__modulo_division():
    assert Calculator().modulus(0) == None


def test_root_memory_less_than_zero():
    with pytest.raises(Exception):
        Calculator().square_root(2)


def test_root_value_less_than_zero():
    with pytest.raises(Exception):
        my_cal = Calculator()
        my_cal.add(16)
        my_cal.square_root(-1)