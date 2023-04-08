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

    def check_bounds(self) -> bool:
        return screen.get_rect().contains(self.rect)

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

# Setup - TIMERS
clock = pygame.time.Clock()
snake_timer = pygame.USEREVENT + 1
pygame.time.set_timer(snake_timer,300)

# Sprites
snake_group = pygame.sprite.GroupSingle()
snake_group.add(Snake())
SS = snake_group.sprite

# Surfaces - NONACTIVe
title = titlefont.render("snake",False,'White')
title_rect = title.get_rect(center = (375,340))
subtitle = subtitlefont.render("the retro game",False,'White')
subtitle_rect = subtitle.get_rect(center=(375,420))

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
                direction = SS.direction
                if direction == "west": SS.rect.x -= 20
                elif direction == "north": SS.rect.y -= 20
                elif direction == "south": SS.rect.y += 20
                else: SS.rect.x += 20
            
            # KEY event (change direction)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and (SS.direction in ["north","south"]): SS.direction = "west"
                elif event.key == pygame.K_UP and (SS.direction in ["west","east"]): SS.direction = "north"
                elif event.key == pygame.K_RIGHT and (SS.direction in ["north","south"]): SS.direction = "east"
                elif event.key == pygame.K_DOWN and (SS.direction in ["west","east"]): SS.direction = "south"
        
        # NONACTIVE-mode events
        else:
            # KEY event (restart game)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                SS.rect.center = (375,375)
                game_active = True

    # what to display in ACTIVE-mode 
    if game_active:

        # check if snake sprite has left screen
        game_active = SS.check_bounds()

        # display screen background, snake
        screen.fill(("#191919"))
        snake_group.draw(screen)
        snake_group.update()

    # what to display in NONACTIVE-mode
    else: 
        screen.fill('#A03A1B')
        screen.blit(title,title_rect)
        screen.blit(subtitle,subtitle_rect)

    # update the whole screen every frame
    pygame.display.update()

    # set frame rate = 60 FPS
    clock.tick_busy_loop(60)