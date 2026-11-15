from .obj_gum import Gum
from game.game_config import GameConfig
import pygame as pg

gconf: GameConfig = GameConfig()


class Pacgum(Gum):
    def __init__(self, grid: list, screen: pg.Surface) -> None:
        super().__init__(grid=grid, screen=screen)
        self.x = len(self.grid[0])
        self.y: int = len(self.grid)

    def instanciate(self) -> list[Pacgum]:
        pacgums: list[Pacgum] = []
        row: int = len(self.grid)
        column: int = len(self.grid[0])

        for i in range(column):
            x: int = (i * gconf.cell) + (gconf.cell // 2) + 1
            for j in range(row):
                y: int = (j * gconf.cell) + (gconf.cell // 2) + 1
                pacgum: Pacgum = Pacgum(self.grid, self.screen)
                pacgum.x = x
                pacgum.y = y
                pacgums.append(pacgum)

        return pacgums
