import pygame
import random

pygame.init()

# Initials
WIDTH, HEIGHT = 1000, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")
run = True
direction = [0, 1]
angle = [0, 1, 2]

# COLORS
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# For Ball
radius = 15
ball_x, ball_y = (WIDTH / 2) - radius, (HEIGHT / 2) - radius
BALL_SPEED = 0.2
ball_vel_x, ball_vel_y = BALL_SPEED, BALL_SPEED

# For Paddle
paddle_width, paddle_height = 20, 120
right_paddle_y = left_paddle_y = (HEIGHT / 2) - (paddle_height / 2)
left_paddle_x, right_paddle_x = 100 - (paddle_width / 2), WIDTH - (
    100 - (paddle_width / 2)
)
right_paddle_vel = left_paddle_vel = 0


def reset_ball():
    global ball_x, ball_y, ball_vel_x, ball_vel_y
    ball_x, ball_y = (WIDTH / 2) - radius, (HEIGHT / 2) - radius
    ball_vel_x = BALL_SPEED * random.choice([-1, 1])
    ball_vel_y = BALL_SPEED * random.choice([-1, 1])


# main Loop
while run:
    win.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                right_paddle_vel = -0.5
            if event.key == pygame.K_DOWN:
                right_paddle_vel = 0.5
            if event.key == pygame.K_w:
                left_paddle_vel = -0.5
            if event.key == pygame.K_s:
                left_paddle_vel = 0.5
        if event.type == pygame.KEYUP:
            right_paddle_vel = 0
            left_paddle_vel = 0

    # Ball Movement Control
    if ball_y <= 0 + radius or ball_y >= HEIGHT - radius:
        ball_vel_y *= -1
    if ball_x >= WIDTH - radius:
        reset_ball()
    if ball_x <= 0 + radius:
        reset_ball()

    # Paddle Movement Control
    right_paddle_y = max(0, min(right_paddle_y, HEIGHT - paddle_height))
    left_paddle_y = max(0, min(left_paddle_y, HEIGHT - paddle_height))

    # Paddle Collisions
    # Left Paddle
    if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
        if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
            ball_x = left_paddle_x + paddle_width
            ball_vel_x *= -1

    # Right Paddle
    if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
        if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
            ball_x = right_paddle_x - radius
            ball_vel_x *= -1

    # Ball Movement
    ball_x += ball_vel_x
    ball_y += ball_vel_y
    right_paddle_y += right_paddle_vel
    left_paddle_y += left_paddle_vel

    pygame.draw.circle(win, BLUE, (int(ball_x), int(ball_y)), radius)
    pygame.draw.rect(
        win, RED, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height)
    )
    pygame.draw.rect(
        win,
        RED,
        pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height),
    )

    pygame.display.update()

pygame.quit()
