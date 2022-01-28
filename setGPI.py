#!/usr/bin/env python3
import RPi.GPIO as GPIO
import sys, getopt
GPIO.setmode(GPIO.BOARD)


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

def main(argv):
    if len(sys.argv) <= 1:
        print('help: setGPI.py -h')
        print('usage: setGPI.py -p (--pin) <pinnumber>')
    else:
        pass
    try:
        opts, args = getopt.getopt(argv,'hp:', ["pin="])
    except getopt.GetoptError:
        print('usage: setGPI.py -p <pinnumber>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("Will set the specified pin to input and read it's value")
            print('usage: setGPI.py -p (--pin) <pinnumber>')
            sys.exit()
        elif opt in ("-p", "--pin"):
            num = arg
            setGPI(int(num)) 

if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        print("Interuppted!")
        exit()