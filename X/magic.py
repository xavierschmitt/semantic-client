from constant import SYSTEMS
from common.operation import Type


def find_system(method, args_types):
    list_all_systems = SYSTEMS['list']
    list_call = {}
    for system in list_all_systems:
        if method in SYSTEMS[system]['method'] and args_types == SYSTEMS[system]['type'].value:
            list_call[system] = SYSTEMS[system][method]

    return list_call


def get_list_of_system(operation):
    method = operation.method
    arg1 = operation.arg1
    arg2 = operation.arg2

    args_types = ""
    if type(arg1) == type(arg2) and type(arg1) in [e.value for e in Type]:
        args_types = type(arg1)
    else:
        print("error type")

    return find_system(method, args_types)


def do_magic(list_operation):

    result = ""
    # for operation in list_operation:
    # get list of system that can perform
    list_call = get_list_of_system(list_operation[0])

    #facto
    for key, value in list_call.iteritems():
        print(key+": " +str(value(list_operation[0].arg1, list_operation[0].arg2)))


