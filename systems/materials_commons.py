""" Materials commons mock system
"""


def add(input_1, input_2):
    """ Concat strings

    Args:
        input_1: string
        input_2: string

    Returns:

    """
    return str(input_1) + str(input_2)


def sub(input_1, input_2):
    """ Replace in input_1 the value of input_2

    Args:
        input_1: string
        input_2: string

    Returns:

    """
    return input_1.replace(input_2, '')
