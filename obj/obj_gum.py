from abc import ABC, abstractmethod
import pygame as pg
from game.game_config import GameConfig

gconf: GameConfig = GameConfig()


class Gum(ABC):
    def __init__(self, grid: list, screen) -> None:
        self.grid: list[list[int]] = grid
        self.screen: pg.Surface = screen
        self.x: int = 0
        self.y: int = 0
        self.size: int = 2
        self.color: tuple[int, int, int] = (255, 215, 0)
        self.points: int = gconf.points_per_pacgum

    def draw(self) -> None:
        pg.draw.circle(self.screen,
                       self.color,
                       (self.x, self.y),
                       self.size)

    @abstractmethod
    def instanciate(self) -> list:
        ...
