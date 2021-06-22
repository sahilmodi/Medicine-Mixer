import math
import time
import argparse

from common import *

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--frequency", type=float, default=4, help="Number of updates per second")
ap.add_argument("-v", "--verbose", action='store_true', help="Print logs")

def motor_controller(timestep):
    thr = math.cos(timestep)
    direc = 1 if thr > 0 else -1
    if 0 < abs(thr) < MIN_MOTOR_SPEED_ABS:
        thr = direc * MIN_MOTOR_SPEED_ABS
    return thr

def main(args):
    timestep = 0
    delay = 1 / args.frequency
    while True:
        throttle = motor_controller(timestep)
        if args.verbose:
            print(f"T={timestep}: {throttle}")
        set_all_motors(throttle)
        time.sleep(delay)
        timestep += math.pi / 6

if __name__ == '__main__':
    args = ap.parse_args()
    main(args)