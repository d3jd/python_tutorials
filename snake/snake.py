import pygame
import sys
import time
import random
from pygame.locals import *

# initializing
pygame.init()

# creating clock
clock = pygame.time.Clock()

# define game screen
screen = pygame.display.set_mode((640, 480))

# set screen title
pygame.display.set_caption("The Snake Game")

# set screen logo
image = pygame.image.load('snake.png')
pygame.display.set_icon(image)

# define colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

# game settings
snakePosition = [100, 100]
snakeSegments = [[100,100], [80,100], [60,100]]
foodPosition = [300, 300]
foodSpawned = 1
direction = 'right'
nextDirection = direction
score = 0
BASE_SPEED = 5
speed = BASE_SPEED

# End Game Scene
def gameOver():
    #print game over message here
    pygame.display.flip()

# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                nextDirection = 'right'
            if event.key == K_LEFT:
                nextDirection = 'left'
            if event.key == K_UP:
                nextDirection = 'up'
            if event.key == K_DOWN:
                nextDirection = 'down'

    #clear the screen to white
    screen.fill(WHITE)

    # move the snake
    if nextDirection == 'right' and not direction == 'left':
        direction = nextDirection
    if nextDirection == 'left' and not direction == 'right':
        direction = nextDirection
    if nextDirection == 'up' and not direction == 'down':
        direction = nextDirection
    if nextDirection == 'down' and not direction == 'up':
        direction = nextDirection

    # update position of the snake head
    if direction == 'right':
        snakePosition[0] += 20
    if direction == 'left':
        snakePosition[0] -= 20
    if direction == 'up':
        snakePosition[1] -= 20
    if direction == 'down':
        snakePosition[1] += 20

    # add the new snake head and pop the tail
    snakeSegments.insert(0, list(snakePosition))
    snakeSegments.pop()

    # draw background
    screen.fill(BLACK)

    # draw the snake body
    for position in snakeSegments[1:]:
        pygame.draw.rect(screen, WHITE, Rect(position[0],position[1],20,20))

    # draw the snake head
    pygame.draw.rect(screen, RED, Rect(snakePosition[0], snakePosition[1],20,20))

    # update display
    pygame.display.flip()

    # update speed with respect to length
    if len(snakeSegments) >= 5:
        speed = BASE_SPEED + len(snakeSegments) // 4
    else:
        speed = BASE_SPEED

    # lock to 10 frames per second
    clock.tick(speed)

pygame.quit()
