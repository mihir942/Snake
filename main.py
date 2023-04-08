from sys import exit
import os
import pygame

# Sprite classes
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()   
        self.image = pygame.Surface([20,20])
        self.image.fill("#21FA90")
        self.rect = self.image.get_rect(center=(375,375))

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
screen = pygame.display.set_mode((750,750))

# Setup - TIMERS
clock = pygame.time.Clock()

# Sprites
snake_group = pygame.sprite.GroupSingle()
snake_group.add(Snake())

while True:

    # loop to check for events
    for event in pygame.event.get():

        # QUIT event
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # display
    screen.fill(("#191919"))
    snake_group.draw(screen)
    snake_group.update()

    # update the whole screen every frame
    pygame.display.update()

    # set frame rate = 60 FPS
    clock.tick_busy_loop(60)