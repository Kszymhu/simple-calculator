from __future__ import annotations
from expression import Expression

class Operations:
    @staticmethod
    def addition(calculated_operands: list[float]) -> float:
        result = calculated_operands[0] + calculated_operands[1]
        return result

    @staticmethod
    def multiplication(calculated_operands: list[float]) -> float:
        result = calculated_operands[0] * calculated_operands[1]
        return result

if __name__ == "__main__":
    expr1 = Expression(Operations.multiplication, [3, 7])
    expr2 = Expression(Operations.addition, [5, expr1])
    print(expr2.calculate())
