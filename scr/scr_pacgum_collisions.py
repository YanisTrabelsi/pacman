def check_pacgums_collision(pacman: type, pacgums: list) -> None:
    for pacgum in pacgums:
        if pacgum.x == pacman.x and pacgum.y == pacman.y:
            pacgums.remove(pacgum)
