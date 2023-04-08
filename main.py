from sys import exit
import os
import pygame

# Functions to load resources
def loadImage(name):
    working_dir = os.path.dirname(__file__)
    return pygame.image.load(working_dir + "/images/" + name)

def loadAudio(name):
    working_dir = os.path.dirname(__file__)
    return pygame.mixer.Sound(working_dir + "/audio/" + name)

def loadFont(name,size):
    working_dir = os.path.dirname(__file__)
    full_path = working_dir + "/font/" + name
    return pygame.font.Font(full_path,size)

# Setup - ADMIN
pygame.init()
pygame.display.set_caption("Snake")
screen = pygame.display.set_mode((400,400))

# Setup - TIMERS
clock = pygame.time.Clock()

# Surfaces - ACTIVE

while True:

    # loop to check for events
    for event in pygame.event.get():

        # QUIT event
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.fill("blue")

    # update the whole screen every frame
    pygame.display.update()

    # set frame rate = 60 FPS
    clock.tick_busy_loop(60)