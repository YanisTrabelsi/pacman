import pygame as pg


class Button():
    def __init__(self,
                 screen: pg.Surface,
                 color: tuple[int, int, int],
                 position: tuple[int, int],
                 text: str | None = None
                 ) -> None:

        self.screen: pg.Surface = screen
        self.color: tuple[int, int, int] = color
        self.position: tuple[int, int] = position
        self.width: int = 600
        self.height: int = 100
        self.shape: tuple[int, int] = (position[0] + self.width,
                                       position[1] + self.height)
        self.border_color: tuple[int, int, int] = (255, 255, 255)
        self.radius: int = 20
        self.border_size: int = 5
        self.show_border: bool = False
        self.is_focused: bool = False
        self.text: str | None = "START"

    def draw(self) -> None:
        if self.show_border:
            pg.draw.rect(self.screen,
                         self.border_color,
                         ((self.position[0] - self.border_size,
                           self.position[1] - self.border_size),
                          (self.shape[0] + self.border_size,
                           self.shape[1] + self.border_size)),
                         border_radius=self.radius)
        pg.draw.rect(self.screen,
                     self.color,
                     (self.position, self.shape),
                     border_radius=self.radius)
        if self.text is not None:
            font: pg.font.Font = pg.font.Font(None, 100)
            text = font.render(self.text, True, (0, 0, 0), None)
            self.screen.blit(text, (self.position[0] + self.width / 2.5,
                                    self.position[1] + self.height / 1.6))


