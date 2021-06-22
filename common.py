import sys
import math
import board
import signal
from adafruit_motorkit import MotorKit


MIN_MOTOR_SPEED_ABS = 0.25

kit = MotorKit(i2c=board.I2C())

def set_motor(motor_id, throttle=0):
    global kit
    assert 1 <= motor_id <= 4, "motor id must between 1-4, inclusive." 
    m = eval(f'kit.motor{motor_id}')
    m.throttle = throttle

def set_all_motors(throttle=0):
    for i in range(4):
        set_motor(i + 1, throttle)

def signal_handler(sig, frame):
    print("\nCtrl-C pressed, stopping motors.")
    set_all_motors()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)