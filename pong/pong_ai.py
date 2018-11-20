#imports
import pygame
import pygame.mixer
import random
import sys

#defining some basic colors
white = 255, 255, 255
black = 0, 0, 0
red = 255, 0, 0
blue = 0, 255, 0
green = 0, 0, 255

#initialize some modules
pygame.init()

#window setup
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Pong")

#image loading
paddle1 = pygame.image.load("Images/paddle.png")
paddle2 = pygame.image.load("Images/paddle.png")
ball = pygame.image.load("Images/ball.png")
bg = pygame.image.load("Images/bg.png")

#game variables
running = True

#position/physics variables
x1 = 5
y1 = 260
x2 = 780
y2 = 260
ball_pos = pygame.math.Vector2(385, 285)
ball_velocity = pygame.math.Vector2(random.randint(-10, 11), random.randint(-10, 11))

#movement variables
paddle1_up = False
paddle1_down = False
paddle2_up = False
paddle2_down = False

#clock...
clock = pygame.time.Clock()

while running:
    #FPS
    clock.tick(60)
    #move ball
    ball_pos += ball_velocity

    #Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                ball_velocity = pygame.math.Vector2(random.randint(-10, 11), random.randint(-10, 11))
                ball_pos = pygame.math.Vector2(385, 285)
            if event.key == pygame.K_f:
                ball_velocity = (ball_velocity * 2)


    # very simple AI
    y1 = ball_pos[1]
    y2 = ball_pos[1]

    #Audio
    #Collision with top and bottom walls
    if ball_pos[1] > window_size[1] - 30:
        ball_velocity[1] = (ball_velocity[1] * -1)

    elif ball_pos[1] < 0:
        ball_velocity[1] = (ball_velocity[1] * -1)

    if ball_pos[0] > window_size[0]:
        ball_velocity = pygame.math.Vector2(random.randint(-10, 11), random.randint(-10, 11))
        ball_pos = pygame.math.Vector2(385, 285)

    if ball_pos[0] < 0:
        ball_velocity = pygame.math.Vector2(random.randint(-10, 11), random.randint(-10, 11))
        ball_pos = pygame.math.Vector2(385, 285)


    #Collision Checking - Still glitchy, but we're getting there
    #New Collision Detection from /u/edbluetooth

    if (0 < int(ball_pos[0]) <=30) and (y1 - 45 < int(ball_pos[1]) <= y1 + 45):
        ball_velocity = (ball_velocity * -1)
        ball_velocity[0] = random.randint(1, 11)
        ball_velocity[1] = random.randint(-10, 11)

    if (750 < int(ball_pos[0]) <= 800 - 30) and (y2 - 45 < int(ball_pos[1]) <= y2 + 45):
        ball_velocity = (ball_velocity * -1)
        ball_velocity[0] = random.randint(-11, -1)
        ball_velocity[1] = random.randint(-10, 11)

    #clear the screen
    screen.fill(white)

    #draw everything again
    screen.blit(bg, (0, 0))
    screen.blit(paddle1, (x1, y1))
    screen.blit(paddle2, (x2, y2))
    screen.blit(ball, ball_pos)

    #render it
    pygame.display.flip()
sys.exit()
