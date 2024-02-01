import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Memory Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)

# Card settings
CARD_WIDTH, CARD_HEIGHT = 100, 100
CARD_GAP = 10
ROWS, COLS = 4, 4
NUM_CARDS = ROWS * COLS // 2

# Images (Update with your own images or use file paths)
IMAGES = [
    pygame.image.load('image1.png'),
    pygame.image.load('image2.png'),
    pygame.image.load('image3.png'),
    pygame.image.load('image4.png'),
    pygame.image.load('image5.png'),
    pygame.image.load('image6.png'),
]

# Shuffle the images and create pairs
random.shuffle(IMAGES)
pairs = IMAGES[:NUM_CARDS] * 2
random.shuffle(pairs)

def draw_card(x, y, image, is_hidden):
    if is_hidden:
        pygame.draw.rect(SCREEN, GRAY, (x, y, CARD_WIDTH, CARD_HEIGHT))
    else:
        SCREEN.blit(pygame.transform.scale(image, (CARD_WIDTH, CARD_HEIGHT)), (x, y))

def main():
    cards = [[False for _ in range(COLS)] for _ in range(ROWS)]
    selected = []
    num_matched = 0
    num_attempts = 0

    while num_matched < NUM_CARDS:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                row, col = y // (CARD_HEIGHT + CARD_GAP), x // (CARD_WIDTH + CARD_GAP)
                if not cards[row][col] and len(selected) < 2:
                    cards[row][col] = True
                    selected.append((row, col))

        SCREEN.fill(BLACK)

        for row in range(ROWS):
            for col in range(COLS):
                x, y = col * (CARD_WIDTH + CARD_GAP), row * (CARD_HEIGHT + CARD_GAP)
                index = row * COLS + col
                is_hidden = not cards[row][col]
                draw_card(x, y, pairs[index], is_hidden)

        pygame.display.update()

        if len(selected) == 2:
            time.sleep(1)  # Show the second card for a short moment
            r1, c1 = selected[0]
            r2, c2 = selected[1]
            if pairs[r1 * COLS + c1] == pairs[r2 * COLS + c2]:
                num_matched += 1
            else:
                cards[r1][c1] = cards[r2][c2] = False
            selected.clear()
            num_attempts += 1

    # Game finished
    print(f"Congratulations! You completed the game in {num_attempts} attempts.")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

if __name__ == "__main__":
    main()
