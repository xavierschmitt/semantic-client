"""
Class Operation
"""

from enum import Enum


class FunctionMethod(Enum):
    ADD = "add"
    SUB = "sub"
    MUL = "mul"
    DIV = "div"


class Type(Enum):
    INT = int
    STR = str


class Operation:

    def __init__(self, method, arg1, arg2):
        self.method = FunctionMethod(method)
        self.arg1 = arg1
        self.arg2 = arg2
