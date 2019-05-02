"""
Class Operation
"""

from enum import Enum


class FunctionMethod(Enum):
    ADD = "add"
    SUB = "sub"


class Type(Enum):
    INT = int
    STR = str


class Operation:

    def __init__(self, method, arg1=None, arg2=None):
        self.method = FunctionMethod(method)
        self.arg1 = arg1
        self.arg2 = arg2
