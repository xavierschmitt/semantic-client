
import sys
from pyke_driver import driver


def main(argv):
    print("Start semantic client with PYKE")
    driver.bc_test("client2")
    # driver.bc_test("client3")


if __name__ == '__main__':
    sys.exit(main(sys.argv))