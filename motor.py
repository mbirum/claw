import RPi.GPIO as GPIO
import time
import motor_seq
import sys
import subprocess
import select

GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)

left_pins = [7,11,13,15]
right_pins = [16,18,22,32]
sleep = 0.001

control_pins = right_pins
sequence = motor_seq.getForwardSequence()

# direction = sys.argv[1]
# if direction == "left":
#     sequence = motor_seq.getBackwardSequence()

# max 512
rotation = 20

# initialize pins
for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)


#-----------------------------
f = subprocess.Popen(['tail', '-F', 'value.txt'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
p = select.poll()
p.register(f.stdout)

while True:
    if p.poll(0.1):
        value = f.stdout.readline()
        value_str = value.decode('utf-8')
        value_str = value_str.replace('\n', '')
        print(f'value: |{value_str}|')
        if "50" == value_str.strip():
            print('move')
            for i in range(int(rotation)):
                for step in range(len(sequence)):
                    for pin in range(4):
                        GPIO.output(control_pins[pin], sequence[step][pin])
                    time.sleep(0.001)
    time.sleep(0.1)



        
GPIO.cleanup()
