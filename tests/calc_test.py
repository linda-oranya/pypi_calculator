import sys
sys.path.append("../src")
import pytest
#from pytest import ExitCode
from calculator import Calculator

calc = Calculator()


def test_add():
    calc = Calculator()
    assert calc.add(10) == 10


def test_subtract():
    calc = Calculator()
    assert calc.subtract(2) == 8


def test_divide():
    calc = Calculator()
    assert calc.divide(2) == 4


def test_memory_val():
    calc = Calculator()
    assert calc.memory_val == 4


def test_multiply():
    calc = Calculator()
    assert calc.multiply(0) == 0


def test_zero_division():
    calc = Calculator()
    assert calc.subtract(20) == -20
    assert calc.add(-10) == -30
    assert calc.divide(0) == None
    assert calc.memory_val == -30


def test_modulus():
    calc = Calculator()
    assert calc.modulus(3) == 0
    assert calc.memory_val == 0


def test_root():
    my_cal = Calculator()
    assert my_cal.add(16) == 16
    assert my_cal.square_root(2) == 4
    with pytest.raises(Exception):
        Calculator().square_root(2)


def test_reset():
    calc = Calculator()
    calc.reset()
    assert calc.memory_val == 0



def test_zero__modulo_division():
    calc = Calculator()
    assert Calculator().modulus(0) == None


def test_root_memory_less_than_zero():
    with pytest.raises(Exception):
        Calculator().square_root(2)


def test_root_value_less_than_zero():
    with pytest.raises(Exception):
        my_cal = Calculator()
        my_cal.add(16)
        my_cal.square_root(-1)

def test_input_validation():
    with pytest.raises(Exception):
        my_cal = Calculator()
        my_cal.add('3')