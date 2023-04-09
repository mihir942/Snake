from sys import exit
import os
import pygame
import pygame.gfxdraw
from random import randrange

# Sprite classes
class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = loadImage('apple.png').convert_alpha()
        self.image = pygame.transform.rotozoom(self.image,0,0.6)
        self.rect = self.image.get_rect(center = (randrange(20,screen_width - 20,20),randrange(20,screen_height - 20,20)))
        
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
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
game_active = False
titlefont = loadFont('babyblues.ttf',150)
subtitlefont = loadFont('babyblues.ttf',30)
scorefont = loadFont('babyblues.ttf',20)

# Setup - SNAKE VARIABLES
S_DIRECTION = "west"
S_LENGTH = 1
S_PATH = []

# Setup - TIMERS
clock = pygame.time.Clock()
snake_timer = pygame.USEREVENT + 1
pygame.time.set_timer(snake_timer,130)

# Sprites
food_group = pygame.sprite.Group()

# Surfaces - ACTIVe
score_apple = loadImage('apple.png').convert_alpha()
score_apple = pygame.transform.rotozoom(score_apple,20,0.6)
score_apple_rect = score_apple.get_rect(center=(570,570))

# Surfaces - NONACTIVE
title = titlefont.render("snake",False,'White')
title_rect = title.get_rect(center = (screen_width//2,270))
subtitle = subtitlefont.render("the retro game",False,'White')
subtitle_rect = subtitle.get_rect(center=(screen_height//2,345))

square = pygame.Surface((12,12),pygame.SRCALPHA)
square_rect = pygame.draw.rect(square,'#21FA90',square.get_rect(),width=0,border_radius=2)
square_rect.center = (337,203)

square2 = pygame.Surface((12,12),pygame.SRCALPHA)
square2_rect = pygame.draw.rect(square2,'#21FA90',square2.get_rect(),width=0,border_radius=2)
square2_rect.center = (352,203)

square3 = pygame.Surface((12,12),pygame.SRCALPHA)
square3_rect = pygame.draw.rect(square3,'#21FA90',square3.get_rect(),width=0,border_radius=2)
square3_rect.center = (367,203)

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
                head,next_pos = S_PATH[0],(0,0)
                if S_DIRECTION == "west":  next_pos = (head[0] - 20,head[1])
                elif S_DIRECTION == "north": next_pos = (head[0],head[1] - 20)
                elif S_DIRECTION == "east": next_pos = (head[0] + 20, head[1])
                else: next_pos = (head[0],head[1] + 20)
                S_PATH.insert(0,next_pos)

            # KEY event (change direction)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and (S_DIRECTION in ["north","south"]): S_DIRECTION = "west"
                elif event.key == pygame.K_UP and (S_DIRECTION in ["west","east"]): S_DIRECTION = "north"
                elif event.key == pygame.K_RIGHT and (S_DIRECTION in ["north","south"]): S_DIRECTION = "east"
                elif event.key == pygame.K_DOWN and (S_DIRECTION in ["west","east"]): S_DIRECTION = "south"
        
        # NONACTIVE-mode events
        else:
            # KEY event (start / restart game)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                start_position = (screen_width//2,screen_height//2)
                S_LENGTH = 1
                S_PATH = [start_position]
                S_DIRECTION = "west"
                game_active = True

    # what to display in ACTIVE-mode 
    if game_active:

        # control snake length
        S_PATH = S_PATH[0:S_LENGTH]

        # generate food if no food
        if not food_group: food_group.add(Food())

        # collision variables
        head = S_PATH[0]
        centerx,centery = head
        coll_rect = pygame.Rect(0,0,10,10)
        coll_rect.center = (centerx,centery)
        
        # collision with food
        if coll_rect.colliderect(food_group.sprites()[0].rect):
            S_LENGTH += 1
            food_group.empty()

        # collision with wall or itself
        conditions = centerx in range(20,580) and centery in range(20,580) and len(set(S_PATH)) == len(S_PATH)
        game_active = conditions

        # display background
        screen.fill(("#191919"))
        food_group.draw(screen)

        # display score
        score = scorefont.render(f"Score: {S_LENGTH - 1} ",False,'White')
        score_rect = score.get_rect(center=(530,570))
        screen.blit(score,score_rect)
        screen.blit(score_apple,score_apple_rect)

        # display snake
        for position in S_PATH:
            snake_surface = pygame.Surface((20,20),pygame.SRCALPHA)
            snake_rect = pygame.draw.rect(snake_surface,'#21FA90',snake_surface.get_rect(),width=0,border_radius=5)
            snake_rect.center=position
            screen.blit(snake_surface,snake_rect)

    # what to display in NONACTIVE-mode
    else: 
        screen.fill('#A03A1B')
        screen.blit(title,title_rect)
        screen.blit(subtitle,subtitle_rect)
        screen.blit(square,square_rect)
        screen.blit(square2,square2_rect)
        screen.blit(square3,square3_rect)

    # update the whole screen every frame
    pygame.display.update()

    # set frame rate = 60 FPS
    clock.tick_busy_loop(60)