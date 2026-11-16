from game import GameConfig

gconf: GameConfig = GameConfig()


def check_pacgums_collision(pacman, pacgums: list) -> None:
    for pacgum in pacgums:
        if pacgum.x == pacman.x and pacgum.y == pacman.y:
            pacgums.remove(pacgum)
            gconf.score += pacgum.score
