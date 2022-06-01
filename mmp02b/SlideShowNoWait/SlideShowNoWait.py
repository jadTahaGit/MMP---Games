__author__ = 'jad'

from pickle import TRUE
import pygame
from pygame.locals import *

background = pygame.Color(255, 228, 95, 0) # background color
sc_w = 356 # screen width
sc_h = 356 # screen height
interval = 4000 # time to display slide

pygame.init()

# Create program display area
screen = pygame.display.set_mode([sc_w, sc_h])
pygame.display.set_caption("Slide Show with Event Loop")

# Set background color
screen.fill(background)

# Preload slide files
slides = []
slides.append(pygame.image.load('mmp02b/SlideShowKeyCtrl/pics/tiger.jpg').convert())
slides.append(pygame.image.load('mmp02b/SlideShowKeyCtrl/pics/elephant.jpg').convert())
slides.append(pygame.image.load('mmp02b/SlideShowKeyCtrl/pics/jbeans.jpg').convert())
slides.append(pygame.image.load('mmp02b/SlideShowKeyCtrl/pics/peppers.jpg').convert())
slides.append(pygame.image.load('mmp02b/SlideShowKeyCtrl/pics/butterfly.jpg').convert())

slideindex = 0
running = True
updatePicture = True

while running:
	if updatePicture:
		screen.blit(slides[slideindex],(50,50))
		pygame.display.update()
		updatePicture = False
		timer = pygame.time.get_ticks() # set timer

	for event in pygame.event.get():
		if event.type == QUIT:
			running = False

	if pygame.time.get_ticks() > timer+interval: # for test purposes, try TRUE here
		slideindex = (slideindex+1)%len(slides)
		updatePicture = True
