""" MDCS mock system
"""


def add(input_1, input_2):
    """ Concat strings

    Args:
        input_1: string
        input_2: string

    Returns:

    """
    return_value = "{0}{1}"
    return return_value.format(input_1, input_2)


def sub(input_1, input_2):
    """ delete all character from input_2 in input_1

    Args:
        input_1: string
        input_2: string

    Returns:

    """
    return_value = input_1
    char_list = list(input_2)
    for character in char_list:
        return_value = return_value.replace(character, '')
    return return_value
