import pygame as pg
from game.game_config import GameConfig

gconf: GameConfig = GameConfig()


def instanciate_pause_ui(screen: pg.Surface) -> list:
    from obj import Button

    center: tuple[int, int] = screen.get_rect().center

    but_start: Button = Button(screen,
                               (0, 0, 255),
                               (center[0],
                                center[1] - gconf.height * 6),
                               "cOntinue")
    but_heigh: Button = Button(screen,
                               (0, 0, 255),
                               (center[0],
                                center[1]),
                               "scOres")
    but_instr: Button = Button(screen,
                               (0, 0, 255),
                               (center[0],
                                center[1] + gconf.height * 6),
                               "instructiOns")
    but_reload: Button = Button(screen,
                                (0, 0, 255),
                                (center[0],
                                 center[1] + gconf.height * 12),
                                "relOAd")

    but_start.is_focused = True

    return [but_start, but_heigh, but_instr, but_reload]


def check_event(but: list) -> int:
    res: int = 0
    if but[0].is_focused:
        res = 0
    elif but[1].is_focused:
        res = 1
    elif but[2].is_focused:
        res = 2
    elif but[3].is_focused:
        res = 4
    return res


def focus_but(but: list, i: int) -> None:
    if but[0].is_focused:
        if i == 1:
            but[0].is_focused = False
            but[1].is_focused = True
    elif but[1].is_focused:
        but[1].is_focused = False
        but[1 + i].is_focused = True
    elif but[2].is_focused:
        but[2].is_focused = False
        but[2 + i].is_focused = True
    elif but[3].is_focused:
        if i == -1:
            but[3].is_focused = False
            but[2].is_focused = True


def draw_pause(screen: pg.Surface, buttons: list) -> int:
    from obj import TextArea

    while True:
        but: list = buttons
        screen.fill((0, 0, 0))

        center: tuple[int, int] = screen.get_rect().center

        pausetxt: TextArea = TextArea(screen,
                                      (center[0], 20),
                                      "pause",
                                      20,
                                      (255, 255, 0))
        pausetxt.draw()

        but[0].draw()
        but[1].draw()
        but[2].draw()
        but[3].draw()

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_DOWN:
                    focus_but(but, 1)
                elif event.key == pg.K_UP:
                    focus_but(but, -1)
                elif event.key == pg.K_RETURN:
                    return check_event(but)
                elif event.key == pg.K_q:
                    return 3

        pg.display.flip()
    return -1
