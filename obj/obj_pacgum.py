from scr.scr_is42 import get42_cells
from .obj_gum import Gum
from game.game_config import GameConfig
import pygame as pg
import random as rd

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
        nb_pacgum: int = gconf.pacgum
        nb_to_remove: int = column * row - nb_pacgum

        for i in range(column):
            x: int = (i * gconf.cell) + (gconf.cell // 2) + 1
            for j in range(row):
                y: int = (j * gconf.cell) + (gconf.cell // 2) + 1
                pacgum: Pacgum = Pacgum(self.grid, self.screen)
                pacgum.x = x
                pacgum.y = y
                pacgums.append(pacgum)

#        for i in range(nb_to_remove):
#            del pacgums[rd.randint(0, len(pacgums))]

        print(len(get42_cells(self.grid)))


        return pacgums
