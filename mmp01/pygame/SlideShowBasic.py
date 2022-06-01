__author__ = 'hussmann'

import pygame
from pygame.locals import *
from sys import exit

background = pygame.Color(255, 228, 95, 0)
sc_w = 356
sc_h = 356

pygame.init()

# Create program display area test
screen = pygame.display.set_mode((sc_w, sc_h))
pygame.display.set_caption("Simple Slide Show")

# Set background color
screen.fill(background)

for event in pygame.event.get():
    if event.type == QUIT:
        exit()

# Load image and show it on screen
slide = pygame.image.load('mmp02b/SlideShowKeyCtrl/pics/tiger.jpg').convert()
screen.blit(slide, (50, 50))
pygame.display.update()
pygame.time.wait(4000)

for event in pygame.event.get():
    if event.type == QUIT:
        exit()

# Load image and show it on screen
slide = pygame.image.load('mmp02b/SlideShowKeyCtrl/pics/elephant.jpg').convert()
screen.blit(slide, (50, 50))
pygame.display.update()
pygame.time.wait(4000)

for event in pygame.event.get():
    if event.type == QUIT:
        exit()

# Load image and show it on screen
slide = pygame.image.load('mmp02b/SlideShowKeyCtrl/pics/jbeans.jpg').convert()
screen.blit(slide, (50, 50))
pygame.display.update()
pygame.time.wait(4000)

for event in pygame.event.get():
    if event.type == QUIT:
        exit()

# Load image and show it on screen
slide = pygame.image.load('mmp02b/SlideShowKeyCtrl/pics/peppers.jpg').convert()
screen.blit(slide, (50,  50))
pygame.display.update()
pygame.time.wait(4000)

for event in pygame.event.get():
    if event.type == QUIT:
        exit()

# Load image and show it on screen
slide = pygame.image.load('mmp02b/SlideShowKeyCtrl/pics/butterfly.jpg').convert()
screen.blit(slide, (50, 50))
pygame.display.update()

# Event loop, just for stopping
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
