import pygame
from pygame.locals import *
from mazegenerator import MazeGenerator

# 1: Nord, 2: Est, 4: Sud, 8: Ouest

CELL = 40
SPEED = 4

pygame.init()  # Init Pygame
screen = pygame.display.set_mode(((CELL * 15) + 2, (CELL * 15) + 50))
clock = pygame.time.Clock()
maze = MazeGenerator()
maze.generate()
grid: list[list[int]] = maze.maze


class PacMan():

    def __init__(self) -> None:

        self.x: int = (7 * CELL) + (CELL // 2) + 1
        self.y: int = (8 * CELL) + (CELL // 2) + 1
        self.direction: str | None = None
        self.wanted_dir: str | None = None


    def can_move(self, direction: str | None) -> bool:

        column: int = self.x // CELL
        line: int = self.y // CELL
        middle_line: int = line * CELL + (CELL // 2) + 1
        middle_column: int = column * CELL + (CELL // 2) + 1
        cell: int = grid[line][column]

        if direction == "left":
            return self.y == middle_line and (not cell & 8 or self.x > middle_column)
        if direction == "right":
            return self.y == middle_line and (not cell & 2 or self.x < middle_column)
        if direction == "up":
            return self.x == middle_column and (not cell & 1 or self.y > middle_line)
        if direction == "down":
            return self.x == middle_column and (not cell & 4 or self.y < middle_line)
        return False

    def move(self) -> None:

        if self.wanted_dir and self.can_move(self.wanted_dir):
            self.direction = self.wanted_dir

        if self.can_move(self.direction):
            if self.direction == "left":
                self.x -= SPEED

            if self.direction == "right":
                self.x += SPEED

            if self.direction == "up":
                self.y -= SPEED

            if self.direction == "down":
                self.y += SPEED


def draw_maze(grid: list[list[int]]):
    x: int = 0
    y: int = 0
    for line in grid:
        for cell in line:
            if cell == 15:
                pygame.draw.rect(screen, (255, 215, 0), (x, y, CELL, CELL))
            if cell & 1:
                pygame.draw.line(screen, (0, 0, 255), (x, y), (x + CELL, y), 2)
            if cell & 2:
                pygame.draw.line(screen, (0, 0, 255), (x + CELL, y), (x + CELL, y + CELL), 2)
            if cell & 4:
                pygame.draw.line(screen, (0, 0, 255), (x, y + CELL), (x + CELL, y + CELL), 2)
            if cell & 8:
                pygame.draw.line(screen, (0, 0, 255), (x, y), (x, y + CELL), 2)

            x = x + CELL
        y = y + CELL
        x = 0


pac_man = PacMan()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        pac_man.wanted_dir = "left"
    if keys[pygame.K_RIGHT]:
        pac_man.wanted_dir = "right"
    if keys[pygame.K_UP]:
        pac_man.wanted_dir = "up"
    if keys[pygame.K_DOWN]:
        pac_man.wanted_dir = "down"

    pac_man.move()

    screen.fill((0, 0, 0))

    draw_maze(grid)
    pygame.draw.circle(screen, (255, 255, 255), (pac_man.x, pac_man.y), 15)

    pygame.draw.circle(screen, (255, 0, 255), ((pac_man.x), (pac_man.y)), 5)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
