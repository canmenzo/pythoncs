import pygame
import random
import sys

# Window and grid settings
WIDTH, HEIGHT = 600, 600
CELL = 20                          # Size of each grid cell in pixels
COLS = WIDTH // CELL               # Number of columns
ROWS = HEIGHT // CELL              # Number of rows
FPS = 10                           # Game speed (frames per second)

# Colors
BLACK  = (0,   0,   0)
GREEN  = (0,   200, 0)
DGREEN = (0,   150, 0)
RED    = (200, 0,   0)
WHITE  = (255, 255, 255)
GRAY   = (40,  40,  40)

def draw_grid(surface):
    """Draw a faint grid so the cells are visible."""
    for x in range(0, WIDTH, CELL):
        pygame.draw.line(surface, GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL):
        pygame.draw.line(surface, GRAY, (0, y), (WIDTH, y))

def random_food(snake):
    """Return a random grid position that is not occupied by the snake."""
    while True:
        pos = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
        if pos not in snake:
            return pos

def draw_cell(surface, pos, color):
    """Draw a single cell at grid position (col, row)."""
    rect = pygame.Rect(pos[0] * CELL + 1, pos[1] * CELL + 1, CELL - 2, CELL - 2)
    pygame.draw.rect(surface, color, rect)

def show_text(surface, text, size, color, y):
    """Render centered text at the given y position."""
    font = pygame.font.SysFont("monospace", size, bold=True)
    label = font.render(text, True, color)
    x = (WIDTH - label.get_width()) // 2
    surface.blit(label, (x, y))

def game_loop(screen, clock):
    # Start the snake in the center of the grid
    snake = [(COLS // 2, ROWS // 2)]
    direction = (1, 0)             # Moving right by default
    next_dir = direction
    food = random_food(snake)
    score = 0
    running = True

    while running:
        clock.tick(FPS)

        # --- Handle input ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP    and direction != (0,  1):
                    next_dir = (0, -1)
                elif event.key == pygame.K_DOWN  and direction != (0, -1):
                    next_dir = (0,  1)
                elif event.key == pygame.K_LEFT  and direction != (1,  0):
                    next_dir = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                    next_dir = (1,  0)

        direction = next_dir

        # --- Move snake: add new head, remove tail unless food eaten ---
        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        # Check wall collision
        if not (0 <= head[0] < COLS and 0 <= head[1] < ROWS):
            return score, "Hit the wall!"

        # Check self collision
        if head in snake:
            return score, "Bit itself!"

        snake.insert(0, head)

        if head == food:
            score += 1
            food = random_food(snake)
        else:
            snake.pop()           # Remove tail only if no food eaten

        # --- Draw ---
        screen.fill(BLACK)
        draw_grid(screen)

        # Draw food
        draw_cell(screen, food, RED)

        # Draw snake (head slightly lighter than body)
        for i, segment in enumerate(snake):
            color = GREEN if i == 0 else DGREEN
            draw_cell(screen, segment, color)

        # Score display
        font = pygame.font.SysFont("monospace", 18)
        score_label = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_label, (5, 5))

        pygame.display.flip()

    return score, ""

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()

    while True:
        # Show start screen
        screen.fill(BLACK)
        show_text(screen, "SNAKE", 60, GREEN, HEIGHT // 3)
        show_text(screen, "Press SPACE to play", 22, WHITE, HEIGHT // 2)
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    waiting = False

        # Play one game
        score, reason = game_loop(screen, clock)

        # Show game over screen
        screen.fill(BLACK)
        show_text(screen, "GAME OVER", 50, RED, HEIGHT // 3 - 30)
        show_text(screen, reason, 24, WHITE, HEIGHT // 3 + 30)
        show_text(screen, f"Score: {score}", 28, GREEN, HEIGHT // 2)
        show_text(screen, "Press SPACE to restart", 20, WHITE, HEIGHT * 2 // 3)
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    waiting = False

if __name__ == "__main__":
    main()
