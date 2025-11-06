import RPi.GPIO as GPIO
import time
import steps
import sys

GPIO.setmode(GPIO.BOARD)

left_pins = [7,11,13,15]
right_pins = [16,18,22,32]
sleep = 0.001

control_pins = right_pins
sequence = steps.getForwardSequence()

direction = sys.argv[1]
if direction == "left":
    sequence = steps.getBackwardSequence()

# max 512
rotation = 20

# initialize pins
for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)
  
for i in range(int(rotation)):
    for step in range(len(sequence)):
        for pin in range(4):
            GPIO.output(control_pins[pin], sequence[step][pin])
        time.sleep(sleep)
        
GPIO.cleanup()
