# A simple game using Pygame in Python

import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Game")

# Set up the clock
clock = pygame.time.Clock()

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the player
player_width = 50
player_height = 50
player_x = (screen_width - player_width) / 2
player_y = screen_height - player_height
player_speed = 5
player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

# Set up the enemy
enemy_width = 50
enemy_height = 50
enemy_x = random.randint(0, screen_width - enemy_width)
enemy_y = 0
enemy_speed = 3
enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)

# Set up the game loop
game_over = False
score = 0
font = pygame.font.SysFont(None, 30)

while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    # Move the enemy
    enemy_y += enemy_speed
    if enemy_y > screen_height:
        enemy_x = random.randint(0, screen_width - enemy_width)
        enemy_y = 0
        score += 1

    # Check for collision
    if player_rect.colliderect(enemy_rect):
        game_over = True

    # Draw the screen
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, player_rect)
    pygame.draw.rect(screen, BLACK, enemy_rect)
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))
    pygame.display.update()

    # Update the clock
    clock.tick(60)

# Clean up Pygame
pygame.quit()
