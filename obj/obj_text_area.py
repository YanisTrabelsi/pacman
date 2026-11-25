import pygame as pg
from game.game_config import GameConfig

gconf: GameConfig = GameConfig()


class TextArea:
    def __init__(self,
                 screen: pg.Surface,
                 pos: tuple[int, int],
                 text: str,
                 font_size: int,
                 text_color: tuple[int, int, int],
                 bg_color: tuple[int, int, int] | None = None,
                 font: str | None = "res/Pacfont-ZEBZ.ttf"):
        self.screen: pg.Surface = screen
        self.pos: tuple[int, int] = pos
        self.text: str = text
        self.font_size: int = font_size
        self.text_color: tuple[int, int, int] = text_color
        self.bg_color: tuple[int, int, int] | None = bg_color
        self.font = font

    def draw(self) -> None:
        font: pg.font.Font = pg.font.Font(self.font, self.font_size)
        text = font.render(self.text, True, self.text_color, self.bg_color)
        text_rect = text.get_rect()
        text_rect.centerx = self.pos[0]
        text_rect.y = self.pos[1]
        self.screen.blit(text, text_rect)
