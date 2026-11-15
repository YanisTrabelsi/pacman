from abc import ABC
import pygame as pg
from game.game_config import GameConfig

gconf: GameConfig = GameConfig()


class Gum(ABC):
    def __init__(self, grid: list, screen) -> None:
        self.is_eaten: bool = False
        self.screen: pg.Surface = screen
        self.x: int = 0
        self.y: int = 0
        self.size: int = 4

    def draw(self) -> None:
        pg.draw.circle(self.screen,
                       (255, 255, 255),
                       (self.x, self.y),
                       gconf.cell // self.size)
