### Calculator 

This is a python package hosted on PYPI and can be used to perform basic functions on calculator such as;
- ADDITION
- SUBTRACTION
- DIVISION
- MULTIPLICATION

It has the MIT License and is deploy on PyPI using Git.

### Installation


The package can be installed via PYPI

$ pip install pypi_calculator
Installation via Github this is for the stable released version

$ pip install git+https://github.com/linda-oranya/CALCULATOR


### Usage
The calculator can be used for basic mathematical computation. The calculator has a memory that can reset itself to 0 and also stores previous values, except the memory is reset


Sample Code
from calculator import Calculator

cal = Calculator()
#### Addition
>>> cal.add(10)
10

#### Subtraction
subtract

>>> cal.subtract(2)
8
because the memory was not reset, 2 was subtracted from previous value 10

Division
For divide, zero division returns None and description

>>> cal.divide(2)
4
>>> cal.divide(0)
number cannot be zero => float division by zero
None

>>> cal.memory_val
4


