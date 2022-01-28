# Raspberry-Pi-GPIO
Control the GPIO pins on the Raspberry Pi's Interface(s) with Python,
using the RPI.GPIO Library.  
⚠ The pin numbers used here are equal to the boards layout **GPIO.setmode(GPIO.BOARD)**. ⚠  
This means that pin 1 is not equal to the GPIO pin 1.


#### setGPI.py :
Set the specified pin (-p or --pin) to input and read it. 

*Example:*  
*python3 setGPI.py -p 15*

#### setGPO.py :
Set the specified pin (-p or --pin) to output and set the specified state (-s or --state), either high or low.

*Example:*   
*python3 setGPO.py -p 15 -s high*

#### readSequence.py :
Set the specified pin (-p or --pin) to input and log every state while on a specified timer (-t or --time) with a specified delay (-d or --delay) between logs.  
This will log to a file (log1.txt).

*Example:*  
*python3 readSequence.py -p 15 -t 10 -d 1*
