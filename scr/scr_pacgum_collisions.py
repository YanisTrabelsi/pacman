from obj import Pacman, Pacgum


def check_pacgums_collision(pacman: Pacman, pacgums: list[Pacgum]) -> None:
    for pacgum in pacgums:
        if pacgum.x == pacman.x and pacgum.y == pacman.y:
            pacgum.is_eaten = True
