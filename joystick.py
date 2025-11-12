import pygame
import os
import RPi.GPIO as GPIO
import time
import motor_seq
import sys
import subprocess
import select

GPIO.setmode(GPIO.BOARD)

left_pins = [7,11,13,15]
right_pins = [16,18,22,32]
sleep = 0.001

control_pins = right_pins
sequence = motor_seq.getForwardSequence()

# max 512
rotation = 20

# initialize pins
for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)

pygame.init()
pygame.joystick.init()

joystick_count = pygame.joystick.get_count()
if joystick_count < 1:
	print("No joystick found")
else:
	joystick = pygame.joystick.Joystick(0)
	joystick.init()
	print("Initialized joystick")
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.JOYBUTTONDOWN:
				print(f"Button {event.button} pressed")
			elif event.type == pygame.JOYBUTTONUP:
				print(f"Button {event.button} released")
			elif event.type == pygame.JOYAXISMOTION and event.axis == 0:
				if event.value < 0:
					print(f"left {event.value}")
				elif event.value > 0:
					print(f"right {event.value}")
			elif event.type == pygame.JOYAXISMOTION and event.axis == 1:
				if event.value <= 0.05:
					print(f"up {event.value}")
				elif event.value >= 0.07:
					print(f"down {event.value}")
