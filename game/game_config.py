from dataclasses import asdict, dataclass
from .game_config_error_handler import check_data
import json

file: str = "config.json"
try:
    with open(file, 'a+') as data:
        if data.tell() == 0:
            data.write("{}")
        data.seek(0)
        d: dict = json.load(data)
except PermissionError:
    print("[ERROR] You don't have permissions to open config.json"
          "\nConfig saved in config(1).json")
    file = "config(1).json"
    with open(file, 'a+') as data:
        if data.tell() == 0:
            data.write("{}")
        data.seek(0)
        d: dict = json.load(data)


d = check_data(d)


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
    pacman_spawn: tuple[int, int] = tuple(d["pacman_spawn"])
    ghosts_spawn: tuple[int, int] = tuple(d["ghosts_spawn"])


gconf: GameConfig = GameConfig()
with open(file, 'w') as data:
    json.dump(asdict(gconf), data, indent=4)
