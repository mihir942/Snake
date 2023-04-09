from sys import exit
import os
import pygame
from random import randrange

# Sprite classes
class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20,20])
        self.image.fill('#A03A1B')
        self.rect = self.image.get_rect(center=(randrange(20,740,20),randrange(20,740,20)))

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
game_active = False
titlefont = loadFont('babyblues.ttf',150)
subtitlefont = loadFont('babyblues.ttf',30)

# Setup - SNAKE VARIABLES
S_direction = "west"
S_length = 1
S_path = []

# Setup - TIMERS
clock = pygame.time.Clock()
snake_timer = pygame.USEREVENT + 1
pygame.time.set_timer(snake_timer,200)

# Sprites
food_group = pygame.sprite.Group()

# Surfaces - NONACTIVE
title = titlefont.render("snake",False,'White')
title_rect = title.get_rect(center = (375,340))
subtitle = subtitlefont.render("the retro game",False,'White')
subtitle_rect = subtitle.get_rect(center=(375,420))

# Main Loop
while True:
    
    # loop to check for events
    for event in pygame.event.get():

        # QUIT event
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # ACTIVE-mode events
        if game_active:
            # TIMER event (for snake)
            if event.type == snake_timer:
                head,next_pos = S_path[0],(0,0)
                if S_direction == "west":  next_pos = (head[0] - 20,head[1])
                elif S_direction == "north": next_pos = (head[0],head[1] - 20)
                elif S_direction == "east": next_pos = (head[0] + 20, head[1])
                else: next_pos = (head[0],head[1] + 20)
                S_path.insert(0,next_pos)

            # KEY event (change direction)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and (S_direction in ["north","south"]): S_direction = "west"
                elif event.key == pygame.K_UP and (S_direction in ["west","east"]): S_direction = "north"
                elif event.key == pygame.K_RIGHT and (S_direction in ["north","south"]): S_direction = "east"
                elif event.key == pygame.K_DOWN and (S_direction in ["west","east"]): S_direction = "south"
        
        # NONACTIVE-mode events
        else:
            # KEY event (start / restart game)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                start_position = (380,380)
                S_path.append(start_position)
                S_direction = "west"
                game_active = True

    # what to display in ACTIVE-mode 
    if game_active:

        # control snake length
        S_path = S_path[0:S_length]

        # generate food if no food
        if not food_group: food_group.add(Food())

        # check for collisions
        if S_path[0] == food_group.sprites()[0].rect.center:
            S_length += 1
            food_group.empty()

        # display background
        screen.fill(("#191919"))
        food_group.draw(screen)

        # display snake
        for position in S_path:
            snake_surface = pygame.Surface((20,20))
            snake_rect = pygame.draw.rect(snake_surface,'#21FA90',snake_surface.get_rect(),width=0,border_radius=5)
            snake_rect.center=position
            screen.blit(snake_surface,snake_rect)

    # what to display in NONACTIVE-mode
    else: 
        screen.fill('#A03A1B')
        screen.blit(title,title_rect)
        screen.blit(subtitle,subtitle_rect)

    # update the whole screen every frame
    pygame.display.update()

    # set frame rate = 60 FPS
    clock.tick_busy_loop(60)