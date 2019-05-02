# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('pyke_driver', '', 'functions.kfb'):
           [1556815262.17442, 'functions.fbc'],
         ('pyke_driver', '', 'bc_functions.krb'):
           [1556815458.262717, 'bc_functions_plans.py', 'bc_functions_bc.py'],
        },
        compiler_version)

