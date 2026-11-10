from collections import deque
from .obj_entities import Entity

class Ghost(Entity):
    def __init__(self, grid: list) -> None:
        super().__init__(grid=grid)

    def _can_enter()

    def _find_short_path(self) -> None:
        directions = {"left": (-1, 0), "right": (1, 0), "up": (0, -1), "down": (0, 1)}
        start = (self.x, self.y)
        goal = (pacman.x, pacman.y) 
        previous: dict = {start: None}
        queue = deque([start])
        while queue:
            x, y = queue.popleft()
            if (x, y) == goal:
                break
        for dirs, (dir_x, dir_y) in dirs.items():
            next = (x + dir_x, y + dir_y)
            if next not in prev and self._can_enter(next):

        if goal not in previous:
            return
        letters = []
        current = goal
        while previous[current] is not None:
            parent, letter = previous[current]
            letters.append(letter)
            current = parent
        self._shortest_path = ''.join(reversed(letters))
