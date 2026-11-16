from scr import get42_cells
from .obj_gum import Gum
from game.game_config import GameConfig
import pygame as pg
import random as rd

gconf: GameConfig = GameConfig()


class Pacgum(Gum):
    def __init__(self, grid: list[list[int]], screen: pg.Surface) -> None:
        super().__init__(grid=grid, screen=screen)
        self.x = len(self.grid[0])
        self.y: int = len(self.grid)
        self.color = (255, 0, 0)

    def instanciate(self) -> list[Pacgum]:
        pacgums: list[Pacgum] = []
        row: int = len(self.grid)
        column: int = len(self.grid[0])
        pacgum_padding: int = (gconf.cell // 2) + 1
        cells_42: list[tuple[int, int]] = get42_cells(self.grid)
        nb_pacgum: int = gconf.pacgum
        nb_to_remove: int

        for i in range(column):
            x: int = (i * gconf.cell) + pacgum_padding
            for j in range(row):
                y: int = (j * gconf.cell) + pacgum_padding
                pacgum: Pacgum = Pacgum(self.grid, self.screen)
                pacgum.x = x
                pacgum.y = y
                pacgums.append(pacgum)

        for cell in cells_42:
            for pacgum in pacgums:
                if pacgum.x == cell[0] + pacgum_padding and pacgum.y == cell[1] + pacgum_padding:
                    pacgums.remove(pacgum)

        nb_to_remove = len(pacgums) - nb_pacgum
        for i in range(nb_to_remove):
            pacgum: Pacgum = rd.choice(pacgums)
            pacgums.remove(pacgum)

        return pacgums
