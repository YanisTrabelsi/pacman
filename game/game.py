import pygame as pg
from .game_config import Game_config


d: Game_config = Game_config()


class Game():
    def __init__(self, screen: pg.Surface, grid: list):
        self.screen = screen
        self.grid = grid
        self.cell = d.cell

    def draw_maze(self):
        x: int = 0
        y: int = 0
        for line in self.grid:
            for cell in line:
                if cell == 15:
                    pg.draw.rect(self.screen, (255, 215, 0), (x, y, self.cell, self.cell))
                if cell & 1:
                    pg.draw.line(self.screen, (0, 0, 255), (x, y), (x + self.cell, y), 2)
                if cell & 2:
                    pg.draw.line(self.screen, (0, 0, 255), (x + self.cell, y), (x + self.cell, y + self.cell), 2)
                if cell & 4:
                    pg.draw.line(self.screen, (0, 0, 255), (x, y + self.cell), (x + self.cell, y + self.cell), 2)
                if cell & 8:
                    pg.draw.line(self.screen, (0, 0, 255), (x, y), (x, y + self.cell), 2)

                x = x + self.cell
            y = y + self.cell
            x = 0

