from common.operation import FunctionMethod, Operation


def _get_operation(add=False):
    arg1 = None
    arg2 = None
    inputs = "\n".join([e.value for e in FunctionMethod])

    method = raw_input("Input possible:\n"+inputs+"\nPlease enter the operation: ")

    while method not in set(e.value for e in FunctionMethod):
        print("Error the operation is not permitted")
        method = raw_input("Input possible:\n" + inputs + "\nPlease enter the operation: ")

    if not add:
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
    return Operation(method, arg1, arg2)


def generate_request():

    list_operation = []
    list_operation.append(_get_operation())

    yn = raw_input("Do you want to add an operation ? (type 'Y' if yes)")
    while yn == "Y":
        list_operation.append(_get_operation(True))
        yn = raw_input("Do you want to add an operation ? (type 'Y' if yes)")

    # call PYKE with operation
    from X import magic
    magic.do_magic(list_operation)

