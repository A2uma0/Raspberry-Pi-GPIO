#!/usr/bin/env python3
import RPi.GPIO as GPIO
import sys, getopt
from datetime import datetime
from time import sleep
import os
GPIO.setmode(GPIO.BOARD)



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


def main(argv):
    if len(sys.argv) <= 1:
        print('help: setSequence.py -h')
        print('usage: setSequence.py -p (--pin) <pinnumber> -t (--time) <seconds> -d (--delay) <seconds>')
    else:
        pass
    try:
        opts, args = getopt.getopt(argv,'hp:t:d:', ["pin=", "time=", "delay="])
    except getopt.GetoptError:
        print('usage: setSequence.py -p (--pin) <pinnumber> -t (--time) <seconds> -d (--delay) <seconds>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("Will set the specified pin to input and read it's value on a timer with a delay between logs. \nSaves all the logs with timestamps to log.txt")
            print('usage: setSequence.py -p (--pin) <pinnumber> -t (--time) <seconds> -d (--delay) <seconds>')
            sys.exit()
        elif opt in ("-p", "--pin"):
            num = int(arg)
        elif opt in ("-t", "--time"):
            time = int(arg)
        elif opt in ("-d", "--delay"):
            delay = float(arg)
            readSequence(num, time, delay)

if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        print("Interuppted!")
        exit()