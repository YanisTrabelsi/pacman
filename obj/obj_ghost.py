import random
from collections import deque
from .obj_entities import Entity


class Ghost(Entity):

    def __init__(self, grid: list, x: int, y: int) -> None:
        super().__init__(grid=grid)
        self.x: int = (x * self.cell_size) + (self.cell_size // 2) + 1
        self.y: int = (y * self.cell_size) + (self.cell_size // 2) + 1
        self.spawn_x: int = (x * self.cell_size) + (self.cell_size // 2) + 1
        self.spawn_y: int = (y * self.cell_size) + (self.cell_size // 2) + 1
        self.speed: int = 2
        self.wanted_speed: int = 2
        self.is_edible: bool = False
        self.is_eaten: bool = False

    def _is_centered(self) -> bool:
        half = self.cell_size // 2 + 1
        return ((self.x - half) % self.cell_size == 0
                and (self.y - half) % self.cell_size == 0)

    def _can_enter(self, nxt: tuple[int, int], previous: tuple[int, int]) -> bool:

        x, y = nxt

        if not (0 <= y < len(self.grid) and 0 <= x < len(self.grid[0])):
            return False
        if self.grid[y][x] & 1 and previous == (x, y - 1):
            return False
        if self.grid[y][x] & 4 and previous == (x, y + 1):
            return False
        if self.grid[y][x] & 2 and previous == (x + 1, y):
            return False
        if self.grid[y][x] & 8 and previous == (x - 1, y):
            return False
        return True

    def _random_movement(self, start_cell: tuple[int, int]):

        directions = {"left": (-1, 0), "right": (1, 0), "up": (0, -1), "down": (0, 1)}
        opposite = {"left": "right", "right": "left", "up": "down", "down": "up"}

        dirs, nxt = random.choice(list(directions.items()))
        nxt = (start_cell[0] + nxt[0], start_cell[1] + nxt[1])

        if self.direction is not None:
            if self._can_enter(nxt, start_cell) and dirs != opposite[self.direction]:
                self.wanted_dir = dirs
            else:
                self._random_movement(start_cell)

    def _find_short_path(self, goal: tuple[int, int], start_cell: tuple[int, int]) -> None:

        directions = {"left": (-1, 0), "right": (1, 0), "up": (0, -1), "down": (0, 1)}

        previous: dict = {start_cell: None}
        queue = deque([start_cell])
        while queue:
            x, y = queue.popleft()
            if (x, y) == goal:
                break
            for dirs, (dir_x, dir_y) in directions.items():
                nxt = (x + dir_x, y + dir_y)
                if nxt not in previous and self._can_enter(nxt, (x, y)):
                    previous[nxt] = ((x, y), dirs)
                    queue.append(nxt)

        if goal not in previous:
            return
        way = []
        current = goal
        while previous[current] is not None:
            parent, dirs = previous[current]
            way.append(dirs)
            current = parent
        if way:
            self.wanted_dir = way[-1]

    def ghost_move(self, pacman: tuple[int, int]) -> None:

        start_cell: tuple[int, int] = (self.x // self.cell_size, self.y // self.cell_size)
        spawn_cell: tuple[int, int] = (self.spawn_x // self.cell_size, self.spawn_y // self.cell_size)
        pacman_cell: tuple[int, int] = (pacman[0] // self.cell_size, pacman[1] // self.cell_size)

        if self._is_centered():
            self.speed = self.wanted_speed

        if self.is_eaten:
            if start_cell != spawn_cell:
                self._find_short_path(spawn_cell, start_cell)
            else:
                if self._is_centered():
                    self.is_eaten = False
                    self.wanted_speed = 2

        elif start_cell == pacman_cell:
            if self.is_edible:
                self.is_eaten = True
                self.wanted_speed = 4

        else:
            if self._is_centered():
                if self.is_edible:
                    if random.randrange(3) == 1:
                        self._find_short_path(spawn_cell, start_cell)
                    else:
                        self._random_movement(start_cell)
                else:
                    if random.randrange(2) == 1:
                        self._find_short_path(pacman_cell, start_cell)
                    else:
                        self._random_movement(start_cell)
        super().move()
