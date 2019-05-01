from common.operation import FunctionMethod, Operation


def generate_request():

    inputs = "\n".join([e.value for e in FunctionMethod])

    method = raw_input("Input possible:\n"+inputs+"\nPlease enter the operation: ")

    while method not in set(e.value for e in FunctionMethod):
        print("Error the operation is not permitted")
        method = raw_input("Input possible:\n" + inputs + "\nPlease enter the operation: ")

    arg1 = raw_input("Please enter the first argument: ")
    try:
        arg1 = int(arg1)
    except ValueError:
        pass

    arg2 = raw_input("Please enter the second argument: ")
    try:
        arg2 = int(arg2)
    except ValueError:
        pass

    operation = Operation(method, arg1, arg2)

    # call PYKE with operation
