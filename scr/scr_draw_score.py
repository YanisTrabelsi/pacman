import pygame as pg
from game.game_config import GameConfig

gconf: GameConfig = GameConfig()


def instanciate_scores_ui(screen: pg.Surface) -> bool:
    from obj import TextArea
    try:
        with open(gconf.highscore_filename, "r") as f:
            f.close()
    except FileNotFoundError as e:
        print(f"\033[31m[Error]\033[0m {e}")
        return False
    except PermissionError as e:
        print(f"\033[31m[Error]\033[0m {e}")
        return False
    with open(gconf.highscore_filename, "r") as f:
        d: list[str] = f.readlines()

    screen_rect = screen.get_rect()
    text_color: tuple[int, int, int] = (255, 255, 0)
    for i, line in enumerate(d):
        text: TextArea = TextArea(
            screen,
            (screen_rect.centerx,
             (gconf.cell) * i),
            line,
            15,
            text_color,
            font="res/Emulogic-zrEw.ttf"
        )
        text.draw()

    return True


def draw_score(screen: pg.Surface) -> int:

    while True:
        screen.fill((0, 0, 0))
        if not instanciate_scores_ui(screen):
            return -1

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    return False

        pg.display.flip()
    return -1
