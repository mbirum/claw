import pygame
import os

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
				if event.value < 0:
					# print(f"up {event.value}")
					os.system("~/pymotor/env/bin/python3 ~/pymotor/motor.py right &")
				elif event.value > 0:
					print(f"down {event.value}")
