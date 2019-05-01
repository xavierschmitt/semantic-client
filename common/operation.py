"""
Class Operation
"""

from enum import Enum


class FunctionMethod(Enum):
    ADD = "add"
    SUB = "sub"


class Operation:

    def __init__(self, method, arg1, arg2):
        self.operation = FunctionMethod(method)
        self.arg1 = arg1
        self.arg2 = arg2
