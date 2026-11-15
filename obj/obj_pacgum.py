from .obj_gum import Gum
from game.game_config import GameConfig

gconf: GameConfig = GameConfig()


class PacGum(Gum):
    def __init__(self, grid: list) -> None:
        super().__init__(grid=grid)
