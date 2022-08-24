#!/usr/bin/env python3
import RPi.GPIO as GPIO
from datetime import datetime
from time import sleep
import argparse
import os
GPIO.setmode(GPIO.BOARD)

parser = argparse.ArgumentParser(description='Set GPIO pin to input and read it\'s value')
parser.add_argument('--pin', '-p', type=int, help='The pin to set', required=True)
parser.add_argument('--time', '-p', type=int, help='How long to log the value for', required=True)
parser.add_argument('--delay', '-d', type=int, help="Delay between logs", required=True)
args = parser.parse_args()

pin = args.pin
timearg = args.time
delayarg = args.delay



def readSequence(num, time, delay):
        # add number at the end of the filename for unique log files
        counter = 1
        filename = "log{}.txt"
        while os.path.isfile(filename.format(counter)):
            counter += 1
        filename = filename.format(counter)
        # log every state while on a timer with a delay to a log
        print(f"Writing to {filename}...")
        f = open(filename, "a")
        f.close()
        for i in range(time):
            GPIO.setup(num, GPIO.IN)
            f = open(filename, "a")
            if GPIO.input(num):
                b = "High "
            else:
                b = "Low "
            print("Logging state: " + b)
            # write current state with current timestamp
            f.write("\n" + b + "at " + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " on pin: " + str(num))
            f.close()
            # sleep for the specified amount of the delay
            sleep(delay)


def main():
        readSequence(pin, timearg, delayarg)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interuppted!")
        exit()