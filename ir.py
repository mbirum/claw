import os
import RPi.GPIO as GPIO
import time
import motor_seq
import sys
import subprocess
import select
import board
import pulseio
import adafruit_irremote
import os
import time

# GPIO.setmode(GPIO.BOARD)

# left_pins = [7,11,13,15]
# right_pins = [16,18,22,32]
right_pins = [23,24,25,12]
sleep_interval = 0.001

control_pins = right_pins
sequence = motor_seq.getForwardSequence()

# max 512
rotation = 10

# initialize pins
for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)


y_axis_direction = 0
y_axis_speed_factor = 1
x_axis_direction = 0
x_axis_speed_factor = 1

# GPIO.setup(17, GPIO.IN)

ir_receiver = pulseio.PulseIn(board.D17, maxlen=200, idle_state=True)
decoder = adafruit_irremote.NonblockingGenericDecode(ir_receiver)

while True:
  try:
    for message in decoder.read():
      y_axis_direction = 0
      if isinstance(message, adafruit_irremote.IRMessage):
          one, two, three, four = message.code
          print(four)
          if "4" == str(four): # up
              y_axis_direction = 1
          elif "187" == str(four): # down
              y_axis_direction = -1
          elif "51" == str(four): # left
              y_axis_direction = -1
          elif "85" == str(four): # right
              y_axis_direction = 1
      if y_axis_direction < 0:
        sequence = motor_seq.getForwardSequence()
        for i in range(int(rotation)):
          for step in range(len(sequence)):
            for pin in range(4):
              GPIO.output(control_pins[pin], sequence[step][pin])
            time.sleep(sleep_interval)
      elif y_axis_direction > 0:
        sequence = motor_seq.getBackwardSequence()
        for i in range(int(rotation)):
          for step in range(len(sequence)):
            for pin in range(4):
              GPIO.output(control_pins[pin], sequence[step][pin])
            time.sleep(sleep_interval)
      else:
        print("Error decoding")
        y_axis_direction = 0
  except Exception as e:
    print(f"error - {e}")
