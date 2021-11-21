"""Holds the Operations class.
"""

class Operations:
    """Contains methods used for calculations.
    """

    @staticmethod
    def addition(operands: list[float]) -> float:
        """Adds all operands together.
        Operands don't need to fit any requirements.
        Raises ValueError if less than two operands.
        """

        if len(operands) < 2:
            raise ValueError

        result: float = operands[0]
        for operand in operands[1:]:
            result += operand

        return result

    @staticmethod
    def subtraction(operands: list[float]) -> float:
        """Subtracts all operands (without the first) from the first one.
        Operands don't need to fit any requirements.
        Raises ValueError if less than two operands.
        """

        if len(operands) < 2:
            raise ValueError

        result: float = operands[0]
        for operand in operands[1:]:
            result -= operand

        return result

    @staticmethod
    def multiplication(operands: list[float]) -> float:
        """Multiplies all operands together.
        Operands don't need to fit any requirements.
        Raises ValueError if less than two operands.
        """

        if len(operands) < 2:
            raise ValueError

        result: float = operands[0]
        for operand in operands[1:]:
            result *= operand

        return result

    @staticmethod
    def division(operands: list[float]) -> float:
        """Divides all operands together.
        Operands don't need to fit any requirements.
        Raises ValueError if less than two operands.
        """

        if len(operands) < 2:
            raise ValueError

        result: float = operands[0]
        for operand in operands[1:]:
            result *= operand

        return result