import pygame as pg
from game.game_config import GameConfig

gconf: GameConfig = GameConfig()


def instanciate_instrctions_ui(screen: pg.Surface) -> None:
    from obj import TextArea

    screen_rect = screen.get_rect()

    instructions = [
        "-UP-  go up",
        "-DOWN-  go down",
        "-LEFT-  go left",
        "-RIGHT-  go right",
        "  -P-  pause",
        "-Q-  quit"
    ]

    commandstxt: TextArea = TextArea(screen,
                                     (screen_rect.centerx,
                                      gconf.height // 2),
                                     "cOmmAnds",
                                     30,
                                     (255, 255, 0))
    commandstxt.draw()
    for i, instruction in enumerate(instructions):
        position: tuple[int, int] = (
            screen_rect.centerx,
            (i + 2) * 40
        )

        text: TextArea = TextArea(
            screen,
            position,
            instruction,
            20,
            (255, 255, 0)
        )

        text.draw()


def draw_instructions(screen: pg.Surface) -> int:
    while True:
        screen.fill((0, 0, 0))

        instanciate_instrctions_ui(screen)

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    return False

        pg.display.flip()
    return -1
