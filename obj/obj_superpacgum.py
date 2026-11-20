from game.game_config import GameConfig
from .obj_gum import Gum
import pygame as pg
import random as rd

gconf: GameConfig = GameConfig()


class Superpacgum(Gum):
    def __init__(self, grid: list[list[int]],
                 screen: pg.Surface, pacgums: list):
        super().__init__(grid=grid, screen=screen)
        self.pacgums: list = pacgums
        self.size: int = 5
        self.score: int = gconf.points_per_super_pacgum
        self.color: tuple[int, int, int] = (255, 255, 255)

    def instanciate(self) -> None:
        row: int = len(self.grid)
        column: int = len(self.grid[0])

        if gconf.rng_super_pacgum:
            rng: int = rd.randrange(row)
            previous: int = rng
            for i in range(0,  len(self.pacgums), row * 3):

                superpacgum: Superpacgum = Superpacgum(self.grid,
                                                       self.screen,
                                                       self.pacgums)

                while (abs(previous - rng) <= column // row // 4):
                    rng: int = rd.randrange(row)
                previous = rng

                try:
                    superpacgum.x = self.pacgums[i + rng].x
                    superpacgum.y = self.pacgums[i + rng].y
                except IndexError:
                    rng = 0
                    superpacgum.x = self.pacgums[i].x
                    superpacgum.y = self.pacgums[i].y
                self.pacgums[i + rng] = superpacgum
        else:
            superpacgum: Superpacgum = Superpacgum(self.grid,
                                                   self.screen,
                                                   self.pacgums)
            superpacgum.x = self.pacgums[0].x
            superpacgum.y = self.pacgums[0].y
            self.pacgums[0] = superpacgum
            superpacgum: Superpacgum = Superpacgum(self.grid,
                                                   self.screen,
                                                   self.pacgums)
            superpacgum.x = self.pacgums[row - 1].x
            superpacgum.y = self.pacgums[row - 1].y
            self.pacgums[row - 1] = superpacgum
            superpacgum: Superpacgum = Superpacgum(self.grid,
                                                   self.screen,
                                                   self.pacgums)
            superpacgum.x = self.pacgums[(row * column) - 19 - row + 1].x
            superpacgum.y = self.pacgums[(row * column) - 19 - row + 1].y
            self.pacgums[(row * column) - 19 - row + 1] = superpacgum
            superpacgum: Superpacgum = Superpacgum(self.grid,
                                                   self.screen,
                                                   self.pacgums)
            superpacgum.x = self.pacgums[(row * column) - 19].x
            superpacgum.y = self.pacgums[(row * column) - 19].y
            self.pacgums[(row * column) - 19] = superpacgum
            superpacgum: Superpacgum = Superpacgum(self.grid,
                                                   self.screen,
                                                   self.pacgums)
