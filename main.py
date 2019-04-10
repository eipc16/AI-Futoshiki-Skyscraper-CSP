from Models.FutoshikiModel import FutoshikiModel
from Models.SkyscraperModel import SkyscraperModel
from Algorithms.ForwardChecking import ForwardChecking
from Algorithms.BackTracking import BackTracking

import sys, os


def start(csp_model, algo='forward_checking'):
    if algo == 'forward_checking':
        print('Running forward checking...')
        csp = ForwardChecking(csp_model)
    else:
        print('Running back tracking...')
        csp = BackTracking(csp_model)

    csp.run()


if __name__ == "__main__":
    if len(sys.argv) > 2:
        method = "forward_checking" if sys.argv[1] == "fc" else "back_tracking"
        fn = sys.argv[2]
    else:
        method = "forward_checking"
        fn = sys.argv[1]

    if os.path.exists(fn):
        if "futo" in fn:
            print('Starting futoshiki')
            model = FutoshikiModel(fn)
            start(model, algo=method)
        elif "sky" in fn:
            print('Starting Skyscraper')
            model = SkyscraperModel(fn)
            start(model, algo=method)
        else:
            print('Inncorrect file name!')
    else:
        print('You have to provide valid path to the file!')
