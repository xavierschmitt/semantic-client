from constant import SYSTEMS
from common.operation import Type


# def find_system(method, args_types):
#     list_all_systems = SYSTEMS['list']
#     list_call = {}
#     for system in list_all_systems:
#         if method in SYSTEMS[system]['method'] and args_types == SYSTEMS[system]['type'].value:
#             list_call[system] = SYSTEMS[system][method]
#
#     return list_call


# def get_list_of_system(operation):
#     method = operation.method
#     arg1 = operation.arg1
#     arg2 = operation.arg2
#
#     args_types = ""
#     if type(arg1) == type(arg2) and type(arg1) in [e.value for e in Type]:
#         args_types = type(arg1)
#     else:
#         print("error type")
#
#     return find_system(method, args_types)


def get_list_system_capable(list_operation, type):
    list_method = [op.method for op in list_operation]

    list_all_systems = SYSTEMS['list']
    list_call = {}
    for system in list_all_systems:
        if all(elem in SYSTEMS[system]['method'] for elem in list_method) and type == SYSTEMS[system]['type'].value:
            list_call[system] = {}
            for method in list_method:
                list_call[system][method] = SYSTEMS[system][method]
                # list_call[system] = {method: SYSTEMS[system][method]}

    return list_call


def get_type(list_operation):
    args_types = ""
    arg1 = None
    arg2 = None
    for op in list_operation:
        arg2 = op.arg2
        if op.arg1 is not None:
            arg1 = op.arg1
        if type(arg1) == type(arg2) and type(arg1) in [e.value for e in Type]:
            args_types = type(arg1)
        else:
            print("error type")
            args_types = ""
            break

    return args_types


def do_magic(list_operation):

    type = get_type(list_operation)
    list_call = get_list_system_capable(list_operation, type)

    result = 0 #todo fix
    #for operation in list_operation:
        # get list of system that can perform
        #list_call = get_list_of_system(operation)
    for system in list_call.keys():
        result = None
        for operation in list_operation:
            if operation.arg1 is None:
                operation.arg1 = result
            result = list_call[system][operation.method](operation.arg1, operation.arg2)
        print(system+": "+str(result))


        # for key, value in list_call.iteritems():
        #     print(key+": " +str(value(operation.arg1, operation.arg2)))

