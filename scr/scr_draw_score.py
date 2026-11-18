import pygame as pg
from game.game_config import GameConfig

gconf: GameConfig = GameConfig()


def draw_score(screen: pg.Surface) -> int:
    from obj import TextArea

    while True:
        screen.fill((0, 0, 0))

        hello = TextArea(screen,
                         (0, 0),
                         "Scores",
                         100,
                         (0, 0, 0),
                         (255, 255, 255))

        hello.draw()

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    return False

        pg.display.flip()
    return -1
