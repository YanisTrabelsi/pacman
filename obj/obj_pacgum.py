from .obj_gum import Gum
from game.game_config import GameConfig
import pygame as pg

gconf: GameConfig = GameConfig()


class PacGum(Gum):
    def __init__(self, grid: list, screen: pg.Surface) -> None:
        super().__init__(grid=grid, screen=screen)
