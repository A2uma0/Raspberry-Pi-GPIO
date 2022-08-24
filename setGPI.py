#!/usr/bin/env python3
import RPi.GPIO as GPIO
import argparse
GPIO.setmode(GPIO.BOARD)


parser = argparse.ArgumentParser(description='Set GPIO pin to input and read it\'s value')
parser.add_argument('--pin', '-p', type=int, help='The pin to set', required=True)
args = parser.parse_args()

pin = args.pin

def setGPI(num):
    # set up input channel without pull-up
    try:
        GPIO.setup(num, GPIO.IN)
    # catch exception 
    except ValueError as e:
        print(" Invalid Channel, check if the pin is a GPIO pin.")
        exit()
    except Exception as s:
        print("An Error ocurred.")
        print(s)
        exit()
    # check for H/L
    if GPIO.input(num):
        print(f" Pin {num} is HIGH!")
    else:
        print(f" Pin {num} is LOW!")

def main():
        setGPI(pin) 

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interuppted!")
        exit()