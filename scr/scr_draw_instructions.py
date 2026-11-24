import pygame as pg
from game.game_config import GameConfig

gconf: GameConfig = GameConfig()


def instanciate_instrctions_ui(screen: pg.Surface) -> None:
    from obj import TextArea

    screen_rect = screen.get_rect()
    text_color: tuple[int, int, int] = (255, 255, 0)

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
                                      gconf.height),
                                     "cOmmAnds",
                                     30,
                                     text_color,
                                     font="res/Emulogic-zrEw.ttf")
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
            text_color
        )

        text.draw()
    howtotxt: TextArea = TextArea(screen,
                                  (screen_rect.centerx,
                                   gconf.height * (gconf.cell // 2) + 50),
                                  "hOw tO plAy",
                                  30,
                                  text_color,
                                  font="res/Emulogic-zrEw.ttf")
    howtotxt.draw()
    rules = (
        "to win collect all pacgums.\n"
        "avoid ghosts or you lose a life.\n"
        "eat super-pacgums to eat them !")
    for i, line in enumerate(rules.split("\n")):
        rulestxt: TextArea = TextArea(screen,
                                      (screen_rect.centerx,
                                       gconf.height * (((gconf.cell // 2) + (i + 2) * 2)) + 50),
                                      line,
                                      13,
                                      text_color,
                                      font="res/Emulogic-zrEw.ttf")
        rulestxt.draw()



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
