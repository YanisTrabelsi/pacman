from dataclasses import asdict, dataclass
from .game_config_error_handler import check_data
import json

file: str = "config.json"
try:
    with open(file, 'a+') as data:
        if data.tell() == 0:
            data.write("{}")
        data.seek(0)
        for line in data.readlines():
            if '{' in line or '}' in line:
                continue
            print(repr(line))
            try:
                json.loads(f"{{{line.translate(str.maketrans('', '', ', \t\n'))}}}")
            except json.JSONDecodeError:
                print("ERROOOOOR")
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
    pacman_spawn_x: int = d["pacman_spawn_x"]
    pacman_spawn_y: int = d["pacman_spawn_y"]
    ghosts_spawn_x: int = d["ghosts_spawn_x"]
    ghosts_spawn_y: int = d["ghosts_spawn_y"]


gconf: GameConfig = GameConfig()
with open(file, 'w') as data:
    json.dump(asdict(gconf), data, indent=4)
