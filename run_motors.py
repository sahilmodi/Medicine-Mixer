# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""Simple test for using adafruit_motorkit with a DC motor"""
import time
import board
from adafruit_motorkit import MotorKit

kit = MotorKit(i2c=board.I2C())

def set_all_motors(throttle=0):
    global kit
    motors = [eval(f'kit.motor{i}') for i in range(1, 5)]
    for m in motors:
        m.throttle = throttle

set_all_motors(1.0)
time.sleep(1.0)
set_all_motors()
time.sleep(0.25)
set_all_motors(-1.0)
time.sleep(1.0)
set_all_motors()
