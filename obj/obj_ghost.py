from collections import deque
from .obj_entities import Entity

class Ghost(Entity):
    def __init__(self, grid: list) -> None:
        super().__init__(grid=grid)

    def _can_enter(self, next: tuple[int, int], previous: tuple[int, int]) -> bool:
        if self.grid[next[1]][next[0]] & 1 and previous == (next[0], next[1] - 1):
            return False
        if self.grid[next[1]][next[0]] & 4 and previous == (next[0], next[1] + 1):
            return False
        if self.grid[next[1]][next[0]] & 2 and previous == (next[0] + 1, next[1]):
            return False
        if self.grid[next[1]][next[0]] & 8 and previous == (next[0] - 1, next[1]):
            return False
        return True

    def _find_short_path(self) -> None:
        directions = {"left": (-1, 0), "right": (1, 0), "up": (0, -1), "down": (0, 1)}
        start = (self.x // self.cell_size, self.y // self.cell_size)
        goal = (pacman.x // self.cell_size, pacman.y // self.cell_size)
        previous: dict = {start: None}
        queue = deque([start])
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
        self.wanted_dir = way[-1]
