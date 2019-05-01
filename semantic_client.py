import sys
from request_handler import generate_request


def main(argv):
    print("Start semantic client")
    generate_request.generate_request()

if __name__ == '__main__':
    sys.exit(main(sys.argv))
