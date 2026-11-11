from .obj_entities import Entity
from pygame import key, K_LEFT, K_RIGHT, K_UP, K_DOWN
from game.game_config import GameConfig


gconf: GameConfig = GameConfig()


class Pacman(Entity):
    def __init__(self, grid: list) -> None:
        super().__init__(grid=grid)
        self.x = (gconf.pacman_spawn[0] * self.cell_size) + (self.cell_size // 2) + 1
        self.y = (gconf.pacman_spawn[1] * self.cell_size) + (self.cell_size // 2) + 1

    def get_key_direction(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.wanted_dir = "left"
        if keys[K_RIGHT]:
            self.wanted_dir = "right"
        if keys[K_UP]:
            self.wanted_dir = "up"
        if keys[K_DOWN]:
            self.wanted_dir = "down"

        self.move()
