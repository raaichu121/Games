import pygame
import game_logic
import game_graphics

GRID_SIZE = 4
CELL_SIZE = 100
MARGIN = 10
GRID_WIDTH = GRID_SIZE * (CELL_SIZE + MARGIN) + MARGIN

def main():
    pygame.init()
    win = pygame.display.set_mode((GRID_WIDTH, GRID_WIDTH))
    pygame.display.set_caption("2048 Game")

    # Load and set the game icon
    icon_image = pygame.image.load('icon.png')
    pygame.display.set_icon(icon_image)

    grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

    game_graphics.draw_grid(grid, win) 
    game_logic.add_new_tile(grid)
    game_logic.add_new_tile(grid)
    game_graphics.draw_grid(grid, win)  

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                elif event.key == pygame.K_LEFT:
                    grid, changed = game_logic.move_left(grid)
                elif event.key == pygame.K_RIGHT:
                    grid, changed = game_logic.move_right(grid)
                elif event.key == pygame.K_UP:
                    grid, changed = game_logic.move_up(grid)
                elif event.key == pygame.K_DOWN:
                    grid, changed = game_logic.move_down(grid)

                if changed:
                    game_logic.add_new_tile(grid)
                    game_graphics.draw_grid(grid, win)  

                state = game_logic.get_current_state(grid)
                if state == 'WON':
                    print("You Win!")
                    running = False
                elif state == 'LOST':
                    print("Game Over!")
                    running = False

    pygame.quit()

if __name__ == "__main__":
    main()
