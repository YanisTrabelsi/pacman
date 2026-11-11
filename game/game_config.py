from dataclasses import dataclass
import json


with open('config.json', 'r') as data:
    d: dict = json.load(data)


@dataclass
class GameConfig:
    highscore_filename: str = d["highscore_filename"]
    width: int = d["width"]
    height: int = d["height"]
    lives: int = d["lives"]
    pacgum: int = d["pacgum"]
    points_per_pacgum: int = d["points_per_pacgum"]
    points_per_super_pacgum: int = d["points_per_super_pacgum"]
    points_per_ghost: int = d["points_per_ghost"]
    seed: int = d["seed"]
    level_max_time: int = d["level_max_time"]
    cell: int = d["cell"]
    speed: int = d["speed"]
