import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tower of Hanoi 3D")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Tower settings
NUM_TOWERS = 3
TOWER_WIDTH = 20
TOWER_HEIGHT = 300
TOWER_COLOR = RED
TOWER_GAP = 200

# Disc settings
NUM_DISCS = 5
DISC_WIDTH_FACTOR = 30
DISC_HEIGHT = 20
DISC_COLOR = GREEN
DISC_GAP = 10

# Disc movement settings
SPEED = 5


def draw_tower(x, y):
    pygame.draw.rect(SCREEN, TOWER_COLOR, (x, y, TOWER_WIDTH, TOWER_HEIGHT))


def draw_disc(x, y, width):
    pygame.draw.rect(SCREEN, DISC_COLOR, (x, y, width, DISC_HEIGHT))


def draw_initial_state(tower_positions, disc_sizes):
    for i in range(NUM_TOWERS):
        draw_tower(tower_positions[i], SCREEN_HEIGHT - TOWER_HEIGHT)
        for j in range(len(disc_sizes[i])):
            disc_width = disc_sizes[i][j] * DISC_WIDTH_FACTOR
            draw_disc(tower_positions[i] - disc_width / 2, SCREEN_HEIGHT - (j + 1) * (DISC_HEIGHT + DISC_GAP),
                      disc_width)


def move_disc(source_tower, target_tower, disc_sizes):
    if len(disc_sizes[source_tower]) > 0:
        disc = disc_sizes[source_tower].pop()
        disc_sizes[target_tower].append(disc)


def tower_of_hanoi(n, source, auxiliary, target, disc_sizes):
    if n > 0:
        tower_of_hanoi(n - 1, source, target, auxiliary, disc_sizes)
        move_disc(source, target, disc_sizes)
        draw_state(disc_sizes)
        pygame.time.delay(500)
        pygame.display.update()
        tower_of_hanoi(n - 1, auxiliary, source, target, disc_sizes)


def draw_state(disc_sizes):
    SCREEN.fill(BLACK)
    for i in range(NUM_TOWERS):
        draw_tower(tower_positions[i], SCREEN_HEIGHT - TOWER_HEIGHT)
        for j in range(len(disc_sizes[i])):
            disc_width = disc_sizes[i][j] * DISC_WIDTH_FACTOR
            draw_disc(tower_positions[i] - disc_width / 2, SCREEN_HEIGHT - (j + 1) * (DISC_HEIGHT + DISC_GAP),
                      disc_width)


if __name__ == "__main__":
    # Initial tower and disc positions
    tower_positions = [SCREEN_WIDTH // 2 - TOWER_WIDTH - TOWER_GAP, SCREEN_WIDTH // 2, SCREEN_WIDTH // 2 + TOWER_WIDTH + TOWER_GAP]
    disc_sizes = [[i + 1 for i in range(NUM_DISCS)], [], []]

    draw_initial_state(tower_positions, disc_sizes)
    pygame.display.update()
    time.sleep(2)

    tower_of_hanoi(NUM_DISCS, 0, 1, 2, disc_sizes)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
