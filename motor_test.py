import time
import argparse

from common import *

ap = argparse.ArgumentParser()
ap.add_argument("--loop", "-l", action="store_true", help="Run script in a loop, Ctrl-C to exit.")


def simple_test():
    set_all_motors(1.0)
    time.sleep(1.0)
    set_all_motors()
    time.sleep(0.25)
    set_all_motors(-1.0)
    time.sleep(1.0)
    set_all_motors()

def main(args):
    if not args.loop:
        simple_test()
        return
    
    while True:
        simple_test()
        time.sleep(1.0)

if __name__ == '__main__':
    args = ap.parse_args()
    main(args)