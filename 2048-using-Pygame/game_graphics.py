import pygame

GRID_SIZE = 4
CELL_SIZE = 100
MARGIN = 10
GRID_WIDTH = GRID_SIZE * (CELL_SIZE + MARGIN) + MARGIN

TILE_COLORS = {
    0: (205, 193, 180),
    2: (255, 215, 128),
    4: (135, 206, 235),
    8: (255, 140, 0),
    16: (0, 149, 255),
    32: (255, 99, 71),
    64: (0, 0, 255),
    128: (240, 230, 140),
    256: (184, 242, 187),
    512: (111, 207, 151),
    1024: (85, 164, 130),
    2048: (52, 101, 104)
}

BACKGROUND_COLOR = (250, 248, 239)
TEXT_COLOR = (117, 110, 101)


def draw_tile(x, y, value, win):
    rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
    color = TILE_COLORS.get(value, (0, 0, 0))
    pygame.draw.rect(win, color, rect)
    if value:
        font = pygame.font.Font(None, 36)
        text = font.render(str(value), True, TEXT_COLOR)
        text_rect = text.get_rect(center=rect.center)
        win.blit(text, text_rect)


def draw_grid(grid, win):
    win.fill(BACKGROUND_COLOR)
    for i, row in enumerate(grid):
        for j, tile_value in enumerate(row):
            x, y = j * (CELL_SIZE + MARGIN) + MARGIN, i * (CELL_SIZE + MARGIN) + MARGIN
            draw_tile(x, y, tile_value, win)
    pygame.display.update()
