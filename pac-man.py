import pygame as pg
import json
from mazegenerator import MazeGenerator
from obj import *

with open('config.json', "r") as json_data:
    data = json.load(json_data)
    print(data)

pg.init()
screen: pg.Surface = pg.display.set_mode(((data["cell"] * 15) + 2, (data["cell"] * 15) + 50))
clock: pg.time.Clock = pg.time.Clock()

maze: MazeGenerator = MazeGenerator()
maze.generate()
grid: list[list[int]] = maze.maze
pacman: Pacman = Pacman(grid)
game: Game = Game(screen, grid)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    pacman.get_key_direction()  # recupere input et move le pacman

    screen.fill((0, 0, 0))

    game.draw_maze()
    pg.draw.circle(screen, (255, 255, 255), (pacman.x, pacman.y), 15)

    pg.display.flip()
    clock.tick(60)

pg.quit()
