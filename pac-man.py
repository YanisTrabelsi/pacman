import pygame as pg
from mazegenerator import MazeGenerator
from obj import *
from scr import *
from game.game import Game
from game.game_config import GameConfig


gconf: GameConfig = GameConfig()

pg.init()
screen: pg.Surface = pg.display.set_mode(((gconf.cell * gconf.width) + 2,
                                          (gconf.cell * gconf.height) + 50))
clock: pg.time.Clock = pg.time.Clock()


def instanciate_game() -> tuple[Game, Pacman]:
    maze = MazeGenerator(size=(gconf.width, gconf.height),
                         seed=gconf.seed)
    maze.generate()
    grid = maze.maze
    game = Game(screen, grid)
    pacman: Pacman = Pacman(grid, screen)
    handler_pacgum: Pacgum = Pacgum(grid, screen)
    game.pacgums = handler_pacgum.instanciate()
    handler_superpacgum: Superpacgum = Superpacgum(grid, screen, game.pacgums)
    handler_superpacgum.instanciate()
    game.menu_ui = instanciate_menu_ui(screen)
    game.pause_ui = instanciate_pause_ui(screen)

    return game, pacman


def main() -> int:
    game, pacman = instanciate_game()
    pacgums = game.pacgums
    menu_ui = game.menu_ui
    pause_ui = game.pause_ui

    running: bool = True
    while running:
        input: int = draw_menu(screen, menu_ui)
        if input == 0:
            ingame: bool = True
            while ingame:
                screen.fill((0, 0, 0))
                game.draw_maze()
                check_pacgums_collision(pacman, pacgums)
                for gum in pacgums:
                    gum.draw()
                pacman.draw()

                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        running = False
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_q:
                            ingame = False
                            running = False
                        if event.key == pg.K_p:
                            input = draw_pause(screen, pause_ui)
                            if input == 1:
                                draw_score(screen)
                            if input == 2:
                                draw_instructions(screen)
                            if input == 4:
                                game, pacman = instanciate_game()
                                pacgums = game.pacgums
                                menu_ui = game.menu_ui
                                pause_ui = game.pause_ui

                pacman.get_key_direction()  # recupere input et move le pacman
                clock.tick(60)
                pg.display.flip()

        if input == 1:
            draw_score(screen)
        if input == 2:
            draw_instructions(screen)
        if input == 3:
            running = False
    pg.quit()
    return 0


main()
