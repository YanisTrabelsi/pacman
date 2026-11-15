from .obj_gum import Gum
from game.game_config import GameConfig
import pygame as pg

gconf: GameConfig = GameConfig()


class PacGum(Gum):
    def __init__(self, grid: list, screen: pg.Surface) -> None:
        super().__init__(grid=grid, screen=screen)

    def instanciate(self) -> None:
        row: int = len(self.grid)
        column: int = len(self.grid[0])
        for i in range(column):
            self.x = (i * gconf.cell) + (gconf.cell // 2) + 1
            for j in range(row):
                self.y = (j * gconf.cell) + (gconf.cell // 2) + 1
                self.draw()
