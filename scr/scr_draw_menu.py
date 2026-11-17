import pygame as pg
from game.game_config import GameConfig

gconf: GameConfig = GameConfig()


def instanciate_menu_ui(screen: pg.Surface) -> list:
    from obj import Button

    center: tuple[int, int] = screen.get_rect().center

    but_start: Button = Button(screen,
                               (0, 0, 255),
                               (center[0],
                                center[1] - gconf.height * 6),
                               "START")
    but_heigh: Button = Button(screen,
                               (0, 0, 255),
                               (center[0],
                                center[1]),
                               "SCORES")
    but_instr: Button = Button(screen,
                               (0, 0, 255),
                               (center[0],
                                center[1] + gconf.height * 6),
                               "INSTRUCTIONS")
    but_start.is_focused = True

    return [but_start, but_heigh, but_instr]


def check_event(but: list) -> int:
    res: int = 0
    if but[0].is_focused:
        res = 0
    elif but[1].is_focused:
        res = 1
    elif but[2].is_focused:
        res = 2
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
        if i == -1:
            but[2].is_focused = False
            but[1].is_focused = True


def draw_menu(screen: pg.Surface, buttons: list) -> int:
    but: list = buttons
    screen.fill((0, 0, 0))

    but[0].draw()
    but[1].draw()
    but[2].draw()

    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:
                focus_but(but, 1)
            elif event.key == pg.K_UP:
                focus_but(but, -1)
            elif event.key == pg.K_RETURN:
                return check_event(but)

    pg.display.flip()
    return -1
