import pygame

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
			elif event.type == pygame.JOYAXISMOTION and event.axis == 3:
				print(f"Axis {event.axis} moved to {event.value}")
