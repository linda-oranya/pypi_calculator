from typing import Union

class Calculator:
    """
        This class performs basic calculator functions such as:
    
        - Addition / Subtraction
        - Multiplication / Division
        - Take (n) root of number
        - Reset memory
    """
    def __init__(self) -> None:
        self.__index = 0

    @property
    def memory_val(self):
        '''
            access the memory which is always set to 0
        '''
        return self.__index

    @staticmethod
    def __input_validation(number: Union[int, float]):
        if not isinstance (number, int) and not isinstance(number, float):
            raise TypeError("only numerical inputs allowed (float or integer)")

    def reset(self):
        """
            Resets memory to 0
        """
        self.__index = 0
       

    def add(self, num: Union[int, float]):
        self.__input_validation(num)
        self.__index += num
        return self.__index

    def subtract(self, num: Union[int, float]):
        self.__input_validation(num)
        self.__index -= num
        return self.__index

    def multiply(self, num: Union[int, float]):
        self.__input_validation(num)
        self.__index *= num
        return self.__index

    def divide(self, num: Union[int, float]):
        self.__input_validation(num)
        try:
            self.__index /= num
            return self.__index
        except ZeroDivisionError as err:
            print(f"number cannot be zero => {err}")

    def modulus(self, num: Union[int, float]):
        self.__input_validation(num)
        try:
            self.__index %= num
            return self.__index
        except ZeroDivisionError as err:
            print(f"number cannot be zero => {err}")

    def square_root(self, num: Union[int, float]):
        self.__input_validation(num)
        if self.__index <= 0:
            raise ValueError(f"memory value must be greater than zero")
        if num <= 0:
            raise ValueError("root must be greater than 0")

        self.__index = self.__index**(1./num)
        return self.__index

