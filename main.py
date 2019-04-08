from Models.FutoshikiModel import FutoshikiModel
from Algorithms.ForwardChecking import ForwardChecking

import sys, os


def main(dir='./Data/Research/test_futo_6_0.txt'):
    model = FutoshikiModel(dir)

    csp = ForwardChecking(model)
    print(csp.get_board(False))
    csp.run()
    print(csp.get_info())
    print(model.validate())
    print(model.validate_non_zero())


if __name__ == "__main__":
    fn = sys.argv[1]
    if os.path.exists(fn):
        main(fn)
    else:
        main()
