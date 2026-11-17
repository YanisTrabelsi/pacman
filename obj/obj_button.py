import pygame as pg
from game.game_config import GameConfig

gconf: GameConfig = GameConfig()


class Button():
    def __init__(self,
                 screen: pg.Surface,
                 color: tuple[int, int, int],
                 pos: tuple[int, int],
                 text: str | None = None
                 ) -> None:

        self.screen: pg.Surface = screen
        self.color: tuple[int, int, int] = color
        self.width: int = gconf.width * 15
        self.height: int = gconf.height * 4
        self.pos: list[int] = [pos[0] - self.width // 2,
                               pos[1] - self.height // 2]
        self.shape: list[int] = [pos[0] + self.width,
                                 pos[1] + self.height]
        self.border_color: tuple[int, int, int] = (100, 150, 150)
        self.radius: int = 20
        self.border_size: int = 2
        self.is_focused: bool = False
        self.text: str | None = text
        self.text_color: tuple[int, int, int] = (200, 200, 200)
        self.font_size: int = (gconf.width + gconf.height)

    def draw(self) -> None:
        if self.is_focused is False:
            self.show_border = True

        rect: pg.Rect = pg.Rect(self.pos, (self.width, self.height))
        border: pg.Rect = pg.Rect([x - self.border_size for x in self.pos],
                                  (self.width + self.border_size,
                                   self.height + self.border_size))
        if not self.is_focused:
            self.text_color = (200, 200, 200)
            pg.draw.rect(self.screen,
                         self.border_color,
                         border,
                         border_radius=self.radius)

            container = pg.draw.rect(self.screen,
                                     self.color,
                                     rect,
                                     border_radius=self.radius)
        else:
            self.text_color = (255, 255, 0)
            rect: pg.Rect = pg.Rect(self.pos,
                                    (self.width // 1.05,
                                     self.height // 1.05))
            container = pg.draw.rect(self.screen,
                                     self.color,
                                     rect,
                                     border_radius=self.radius)

        if self.text is not None:
            font: pg.font.Font = pg.font.Font(None, self.font_size)
            text = font.render(self.text, True, self.text_color, None)
            text_rect = text.get_rect(center=container.center)
            self.screen.blit(text, text_rect)
