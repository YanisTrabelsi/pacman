from game.game_config import GameConfig

gconf: GameConfig = GameConfig()


def create_score_file():
    with open(gconf.highscore_filename, "a+") as f:
        ...
