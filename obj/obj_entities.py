from abc import ABC
import json

with open('config.json', "r") as json_data:
    data = json.load(json_data)
    print(data)


class Entity(ABC):
    def __init__(self, grid: list):
        self.cell_size = data["cell"]
        self.speed = data["speed"]
        self.grid = grid
        self.x: int = (7 * self.cell_size) + (self.cell_size // 2) + 1
        self.y: int = (8 * self.cell_size) + (self.cell_size // 2) + 1
        self.direction: str | None = None
        self.wanted_dir: str | None = None

    def _can_move(self, direction: str | None) -> bool:
        column: int = self.x // self.cell_size
        line: int = self.y // self.cell_size
        middle_line: int = line * self.cell_size + (self.cell_size // 2) + 1
        middle_column: int = column * self.cell_size + (self.cell_size // 2) + 1
        cell: int = self.grid[line][column]

        if direction == "left":
            return self.y == middle_line and (not cell & 8 or self.x > middle_column)
        if direction == "right":
            return self.y == middle_line and (not cell & 2 or self.x < middle_column)
        if direction == "up":
            return self.x == middle_column and (not cell & 1 or self.y > middle_line)
        if direction == "down":
            return self.x == middle_column and (not cell & 4 or self.y < middle_line)
        return False

    def move(self) -> None:

        if self.wanted_dir and self._can_move(self.wanted_dir):
            self.direction = self.wanted_dir

        if self._can_move(self.direction):
            if self.direction == "left":
                self.x -= self.speed

            if self.direction == "right":
                self.x += self.speed

            if self.direction == "up":
                self.y -= self.speed

            if self.direction == "down":
                self.y += self.speed
