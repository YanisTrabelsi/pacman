from abc import ABC


class Gum(ABC):
    def __init__(self, grid: list) -> None:
        self.is_eaten: bool = False
        ...
