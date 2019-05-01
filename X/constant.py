from common.operation import FunctionMethod, Type
from adapters.mdcs import addition as mdcs_addition, subtraction as mdcs_sub
from adapters.hyper_thought import addition as ht_addition, subtraction as ht_sub
from adapters.materials_commons import addition as mc_addition, subtraction as mc_sub

SYSTEMS = {
    'list': ["MDCS", "HT", "MC"],
    'MDCS': {
        'method': [FunctionMethod.ADD, FunctionMethod.SUB],
        'type': Type.STR,
        FunctionMethod.ADD: mdcs_addition,
        FunctionMethod.SUB: mdcs_sub
    },
    'HT': {
        'method': [FunctionMethod.ADD, FunctionMethod.SUB],
        'type': Type.INT,
        FunctionMethod.ADD: ht_addition,
        FunctionMethod.SUB: ht_sub
    },
    'MC': {
        'method': [FunctionMethod.ADD, FunctionMethod.SUB],
        'type': Type.STR,
        FunctionMethod.ADD: mc_addition,
        FunctionMethod.SUB: mc_sub
    }
}
