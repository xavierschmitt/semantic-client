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
    """ Longest common string

    Args:
        input_1: string
        input_2: string

    Returns:

    """
    return_value = ""
    len1, len2 = len(input_1), len(input_2)
    for i in range(len1):
        match = ""
        for j in range(len2):
            if i + j < len1 and input_1[i + j] == input_2[j]:
                match += input_2[j]
            else:
                if len(match) > len(return_value):
                    return_value = match
                match = ""
    return return_value
