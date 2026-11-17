import pygame as pg
from mazegenerator import MazeGenerator
from obj import *
from scr import *
from game.game import Game
from game.game_config import GameConfig


gconf: GameConfig = GameConfig()

pg.init()
screen: pg.Surface = pg.display.set_mode(((gconf.cell * gconf.width) + 2, (gconf.cell * gconf.height) + 50))
clock: pg.time.Clock = pg.time.Clock()

maze: MazeGenerator = MazeGenerator(size=(gconf.width, gconf.height), seed=gconf.seed)
maze.generate()
grid: list[list[int]] = maze.maze
pacman: Pacman = Pacman(grid, screen)
handler_pacgum: Pacgum = Pacgum(grid, screen)
pacgums: list[Pacgum] = handler_pacgum.instanciate()
handler_superpacgum: Superpacgum = Superpacgum(grid, screen, pacgums)
handler_superpacgum.instanciate()
game: Game = Game(screen, grid)
menu_ui: list = instanciate_menu_ui(screen)


def main() -> int:
    running = True
    while running:
        input: int = draw_menu(screen, menu_ui)
        if input == 0:
            while running:
                screen.fill((0, 0, 0))
                game.draw_maze()
                check_pacgums_collision(pacman, pacgums)
                for gum in pacgums:
                    gum.draw()
                pacman.draw()

                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        running = False

                pacman.get_key_direction()  # recupere input et move le pacman
                clock.tick(60)

                pg.display.flip()
        if input == 1:
            ...
        if input == 3:
            ...

    pg.quit()
    return 0


main()
