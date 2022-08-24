#!/usr/bin/env python3
import RPi.GPIO as GPIO
import argparse
GPIO.setmode(GPIO.BOARD)

parser = argparse.ArgumentParser(description='Set GPIO pin to output and set it\'s value')
parser.add_argument('--pin', '-p', type=int, help='The pin to set', required=True)
parser.add_argument('--state', '-s', type=str, help='The state to set', required=True)
args = parser.parse_args()


def setGPO(num, state):
    # set channel to output with the specified state
    try:
        GPIO.setup(num, GPIO.OUT)
        GPIO.output(num, state)
        if state == 1:
            state = "High"
        elif state == 0:
            state = "Low"
        print(f" Set state: {state} on port {num}")
    except ValueError as e:
        print(e)
        print(" Invalid Channel, check if the pin is a GPIO pin.")
        exit()
    except Exception as s:
        print("An Error ocurred.")
        print(s)
        exit()


def main():
    pin = args.pin
    statearg = args.state
    if statearg == "High" or statearg == "high":
        statearg = GPIO.HIGH
    elif statearg == "Low" or statearg == "low":
        statearg = GPIO.LOW
    else:
        print(" Not a valid state!")
    setGPO(pin, statearg)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interuppted!")
        exit()