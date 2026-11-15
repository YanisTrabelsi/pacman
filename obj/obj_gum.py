from abc import ABC, abstractmethod
import pygame as pg
from game.game_config import GameConfig

gconf: GameConfig = GameConfig()


class Gum(ABC):
    def __init__(self, grid: list, screen) -> None:
        self.grid: list[list[int]] = grid
        self.screen: pg.Surface = screen
        self.is_eaten: bool = False
        self.x: int = 0
        self.y: int = 0
        self.size: int = 2
        self.color: tuple[int, int, int] = (255, 215, 0)

    def draw(self) -> None:
        if not self.is_eaten:
            pg.draw.circle(self.screen,
                           self.color,
                           (self.x, self.y),
                           self.size)
        else:
            pg.draw.circle(self.screen,
                           (0, 0, 0),
                           (self.x, self.y),
                           self.size)

    @abstractmethod
    def instanciate(self) -> list:
        ...
