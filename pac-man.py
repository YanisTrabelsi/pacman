import pygame as pg
from mazegenerator import MazeGenerator
from obj import *
from game.game import Game
from game.game_config import GameConfig


gconf: GameConfig = GameConfig()

pg.init()
screen: pg.Surface = pg.display.set_mode(((gconf.cell * gconf.width) + 2, (gconf.cell * gconf.height) + 50))
clock: pg.time.Clock = pg.time.Clock()

maze: MazeGenerator = MazeGenerator(size=(gconf.width, gconf.height), seed=gconf.seed)
maze.generate()
grid: list[list[int]] = maze.maze
pacman: Pacman = Pacman(grid)
game: Game = Game(screen, grid)


def main() -> int:
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        pacman.get_key_direction()  # recupere input et move le pacman

        screen.fill((0, 0, 0))

        game.draw_maze()
        pg.draw.circle(screen,
                       (255, 255, 255),
                       (pacman.x, pacman.y),
                       gconf.cell // 3)

        pg.display.flip()
        clock.tick(60)

    pg.quit()
    return 0


main()
