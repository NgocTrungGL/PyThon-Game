import pygame

pygame.init()
WIDTH = 800
HEIGHT = 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)
CIRCLE_CENTER = [WIDTH/2, HEIGHT/2]
CIRCLE_RADIUS = 150
BALL_RADIUS = 5
BALL_POS = [WIDTH/2, HEIGHT/2 - 120]

running = True
GRAVITY = 0.2 
ball_vel =  [0, 0]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    ball_vel[1] += GRAVITY
    BALL_POS[0] += ball_vel[0]
    BALL_POS[1] += ball_vel[1]
    window.fill(BLACK)
    pygame.draw.circle(window, ORANGE, CIRCLE_CENTER, CIRCLE_RADIUS, 3)
    pygame.draw.circle(window, RED, BALL_POS, BALL_RADIUS)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()