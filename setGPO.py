#!/usr/bin/env python3
import RPi.GPIO as GPIO
import sys, getopt
GPIO.setmode(GPIO.BOARD)



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


def main(argv):
    if len(sys.argv) <= 1:
        print('help: setGPO.py -h')
        print('usage: setGPO.py -p (--pin) <pinnumber> -s (--state) <high/low>')
    else:
        pass
    try:
        opts, args = getopt.getopt(argv,'hp:s:', ["pin=", "state="])
    except getopt.GetoptError:
        print('usage: setGPO.py -p (--pin) <pinnumber> -s (--state) <high/low>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("Will set the specified pin to output and set it to the specified state")
            print('usage: setGPO.py -p (--pin) <pinnumber> -s (--state) <high/low>')
            sys.exit()
        elif opt in ("-p", "--pin"):
            num = int(arg)
        elif opt in ("-s", "--state"):
            if arg == "High" or arg == "high":
                state = GPIO.HIGH
            elif arg == "Low" or arg == "low":
                state = GPIO.LOW
            else:
                print(" Not a valid state!")
            setGPO(num, state)

if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        print("Interuppted!")
        exit()