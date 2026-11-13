from dataclasses import asdict, dataclass
from .game_config_error_handler import check_data
import json

file: str = "config.json"
try:
    with open(file, "a+") as data:
        if data.tell() == 0:
            data.write("{}")
        data.seek(0)

        lines: list[str] = data.readlines()
        len_lines: int = len(lines) - 1
        while '{' not in lines[0] or\
                len(lines[1].translate(str.maketrans('', '', ', \n\t\r'))) < 3:
            del lines[0]
            len_lines -= 1
            continue

        for i, line in enumerate(lines):
            if "{" in line or "}" in line:
                if '{' in line:
                    lines[i] = "{"
                if '}' in line:
                    lines[i] = "}"
                    lines[i - 1] = lines[i - 1].replace(',', '')
                    for e in lines[i + 1:]:
                        del lines[i + 1]
                        len_lines -= 1
                continue
            try:
                json.loads(f"{{{line.translate(str.maketrans('', '', ', \t\n'))}}}")
                if ',' not in line:
                    if i == 0 or i == len_lines - 1:
                        continue
                    else:
                        lines[i] = line.replace('\n', ',\n')
            except json.JSONDecodeError:
                del lines[i]
                len_lines -= 1
                print(f"\033[31m[Error]\033[0m {file} at line {i}")
                print("\033[33m[Notice]\033[0m Deleted or Replaced by default value")
                continue
        with open(file, "w") as f:
            for line in lines:
                f.write(line)
        data.seek(0)
        try:
            d: dict = json.load(data)
        except json.JSONDecodeError as e:
            d: dict = json.loads("{}")
            print(f"\033[31m[Error]\033[0m {e}")
            print("\033[33m[Notice]\033[0m Replaced by default value")
except PermissionError:
    print(
        "\033[31m[Error]\033[0m You don't have permissions to open config.json"
        "\n\033[33m[Notice]\033[0m Config saved in config(1).json"
    )
    file = "config(1).json"
    with open(file, "a+") as data:
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
with open(file, "w") as data:
    json.dump(asdict(gconf), data, indent=4)
