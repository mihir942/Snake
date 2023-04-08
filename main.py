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
        self.direction = "west" 

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
snake_timer = pygame.USEREVENT + 1
pygame.time.set_timer(snake_timer,500)

# Sprites
snake_group = pygame.sprite.GroupSingle()
snake_group.add(Snake())
SS = snake_group.sprite

while True:

    # loop to check for events
    for event in pygame.event.get():

        # QUIT event
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # TIMER event (for snake)
        if event.type == snake_timer:
            direction = SS.direction
            if direction == "west": SS.rect.x -= 20
            elif direction == "north": SS.rect.y -= 20
            elif direction == "south": SS.rect.y += 20
            else: SS.rect.x += 20
        
        # KEY event (change direction)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: SS.direction = "west"
            elif event.key == pygame.K_UP: SS.direction = "north"
            elif event.key == pygame.K_RIGHT: SS.direction = "east"
            elif event.key == pygame.K_DOWN: SS.direction = "south"

    # display
    screen.fill(("#191919"))
    snake_group.draw(screen)
    snake_group.update()

    # update the whole screen every frame
    pygame.display.update()

    # set frame rate = 60 FPS
    clock.tick_busy_loop(60)