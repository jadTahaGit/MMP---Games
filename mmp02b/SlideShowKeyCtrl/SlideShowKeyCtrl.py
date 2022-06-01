__author__ = 'hussmann'

import pygame
from pygame.locals import *
from sys import exit

background = pygame.Color(255,228,95,0) # background color
sc_w = 356 # screen width
sc_h = 356 # screen height
interval = 4000 # time to display slides

pygame.init()

# Create program display area
screen = pygame.display.set_mode([sc_w,sc_h])
pygame.display.set_caption("Slide Show controlled by Arrow Keys")

# Set background color
screen.fill(background)

# Preload slide files
slides = []
slides.append(pygame.image.load('pics/tiger.jpg').convert())
slides.append(pygame.image.load('pics/elephant.jpg').convert())
slides.append(pygame.image.load('pics/jbeans.jpg').convert())
slides.append(pygame.image.load('pics/peppers.jpg').convert())
slides.append(pygame.image.load('pics/butterfly.jpg').convert())

slideindex = 0
running = True
updatePicture = True

# Main loop
while running:

	# Display next picture of necessary
	if updatePicture:
		screen.blit(slides[slideindex],(50,50))
		pygame.display.update()
		updatePicture = False
		timer = pygame.time.get_ticks() # set timer

	# Process events
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False
		if event.type == pygame.KEYUP:
			if event.key in [K_SPACE,K_RIGHT]:
				slideindex = (slideindex+1)%len(slides)
				updatePicture = True
			if event.key == K_LEFT:
				slideindex = (slideindex-1)%len(slides)
				updatePicture = True
			if event.key == K_q:
				running = False

    # Check time interval
	if pygame.time.get_ticks() > timer+interval:
		slideindex = (slideindex+1)%len(slides)
		updatePicture = True
