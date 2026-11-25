import random
from collections import deque
from .obj_entities import Entity
from pygame import Surface


class Ghost(Entity):

    def __init__(self, grid: list, screen: Surface, x: int, y: int) -> None:
        super().__init__(grid=grid, screen=screen)
        self.x: int = (x * self.cell_size) + (self.cell_size // 2) + 1
        self.y: int = (y * self.cell_size) + (self.cell_size // 2) + 1
        self.spawn_x: int = (x * self.cell_size) + (self.cell_size // 2) + 1
        self.spawn_y: int = (y * self.cell_size) + (self.cell_size // 2) + 1
        self.speed: int = 2
        self.wanted_speed: int = 2
        self.is_edible: bool = False
        self.is_eaten: bool = False
        self.is_waiting: bool = False
        self.edible_until: float = 0.0
        self.wait_until: float = 0.0

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

        valid = []
        for dirs, (dx, dy) in directions.items():
            nxt = (start_cell[0] + dx, start_cell[1] + dy)
            if self.direction is not None and dirs == opposite[self.direction]:
                continue
            if self._can_enter(nxt, start_cell):
                valid.append(dirs)

        if valid:
            self.wanted_dir = random.choice(valid)
        else:
            if self.direction is not None:
                self.wanted_dir = opposite[self.direction]

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

    def _edible_time_left(self, now: float) -> float:
        if self.is_edible:
            return max(0.0, self.edible_until - now)
        else:
            return 0.0

    def become_edible(self, now: float) -> None:
        if self.is_eaten:
            return
        self.is_edible = True
        self.wanted_speed = 1
        self.edible_until = now + 6.0

    def ghost_move(self, pacman: tuple[int, int], now: float) -> None:

        start_cell: tuple[int, int] = (self.x // self.cell_size, self.y // self.cell_size)
        spawn_cell: tuple[int, int] = (self.spawn_x // self.cell_size, self.spawn_y // self.cell_size)
        pacman_cell: tuple[int, int] = (pacman[0] // self.cell_size, pacman[1] // self.cell_size)

        if self.is_edible and now >= self.edible_until:
            self.is_edible = False
            self.wanted_speed = 2

        if self.is_waiting:
            if now >= self.wait_until:
                self.is_waiting = False
                self.is_eaten = False
                self.wanted_speed = 2
            else:
                return

        if self._is_centered():
            self.speed = self.wanted_speed

        if self.is_eaten:
            if start_cell != spawn_cell:
                self._find_short_path(spawn_cell, start_cell)
            else:
                if self._is_centered():
                    self.is_waiting = True
                    self.wait_until = now + 4.0
                    return

        elif start_cell == pacman_cell:
            if self.is_edible:
                self.is_eaten = True
                self.is_edible = False
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
